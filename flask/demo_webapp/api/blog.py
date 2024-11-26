from flask import Blueprint
from flask import flash
from flask import jsonify
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from werkzeug.exceptions import NotFound, BadRequest, Unauthorized

from demo_webapp.api.auth import login_required
from demo_webapp.models.Blog import Blog
from demo_webapp.models.User import User
from demo_webapp import db

bp = Blueprint("blog", __name__)

@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    author_id = request.args.get('author_id')
    if author_id:
        posts = (
            db.session.query(Blog, User.username)
            .join(User, Blog.author_id == User.id)
            .filter(Blog.author_id == author_id)
            .all()
        )
    else:
        posts = (
            db.session.query(Blog, User.username)
            .join(User, Blog.author_id == User.id)
            .all()
        )
    #print(posts[0].Blog.title)
    results = [
        {
            "id": post.Blog.id,
            "title": post.Blog.title,
            "body": post.Blog.body,
            "created": post.Blog.created,
            "author_id": post.Blog.author_id,
            "username": post.username,
        }
        for post in posts
    ]
    
    return render_template("blog/index.html", posts=results)


def get_post(id, check_author=True):
    """Get a post and its author by id.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    post = Blog.query.get(id)
    if post is None:
        raise NotFound(f"Blog with ID {id} not found.")

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post["author_id"] != g.user["id"]:
        abort(403)

    return post


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """Create a new blog post."""
    if g.user is None:
        raise Unauthorized("You must be logged in to create a blog post.")
    
    if request.method == "GET":
        return render_template("blog/create.html")
    
    if request.method == "POST":
        # data = request.get_json()
        # if not data or 'title' not in data or 'body' not in data:
        #     raise BadRequest("Title and body are required to create a blog post.")
        title = request.form["title"]
        body = request.form["body"]

        new_blog = Blog(
            title=title,
            body=body,
            author=g.user
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for("blog.index"))
    
    return BadRequest("Invalid Method")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """Update an existing blog post."""
    if g.user is None:
        raise Unauthorized("You must be logged in to update a blog post.")

    post = Blog.query.get(id)
    if post is None:
        raise NotFound(f"Blog with ID {id} not found.")

    if request.method == "GET":
        return render_template("blog/update.html", post=post)
    
    if request.method == "POST":
        if post.author_id != g.user.id:
            raise Unauthorized("You do not have permission to update this blog post.")

        # data = request.get_json()
        # if not data:
        #     raise BadRequest("Request body must contain data to update.")
        # post.title = data.get('title', post.title)
        # post.body = data.get('body', post.body)

        post.title = request.form["title"]
        post.body = request.form["body"]

        db.session.commit()
        return redirect(url_for("blog.index"))
    
    return BadRequest("Invalid Method")


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """Delete a blog post."""
    if g.user is None:
        raise Unauthorized("You must be logged in to delete a blog post.")

    if request.method == "POST":
        blog = Blog.query.get(id)
        if blog is None:
            raise NotFound(f"Blog with ID {id} not found.")

        if blog.author_id != g.user.id:
            raise Unauthorized("You do not have permission to delete this blog post.")

        db.session.delete(blog)
        db.session.commit()
        return redirect(url_for("blog.index"))
    
    return BadRequest("Invalid Method")
