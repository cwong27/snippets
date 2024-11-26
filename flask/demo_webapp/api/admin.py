import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from werkzeug.exceptions import NotFound, BadRequest, Unauthorized

from demo_webapp import db
from demo_webapp.api.auth import login_required
from demo_webapp.models.Blog import Blog
from demo_webapp.models.User import User

bp = Blueprint("admin", __name__, url_prefix="/admin")

@bp.route("/users", methods=("GET", "POST"))
@login_required
def get_users():
    """Users administration"""
    if g.user is None:
        raise Unauthorized("You must be logged in to create a blog post.")
    
    # GET
    if request.method == "GET":
        """
        Fetch users from the database with optional search and pagination.
        """
        # Get search query and pagination parameters
        search_query = request.args.get('q', '').strip()
        page = request.args.get('page', 1, type=int)
        per_page = 5  # Number of users per page

        # Apply search filter if a query is provided
        if search_query:
            query = User.query.filter(User.username.ilike(f'%{search_query}%'))
        else:
            query = User.query

        # Paginate the results
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        users = pagination.items

        # Render the template with user data and pagination
        return render_template('admin/users.html', users=users, pagination=pagination, search_query=search_query)
    
    # POST
    if request.method == "POST":
        return redirect(url_for("blog.index"))
    
    return BadRequest("Invalid Method")