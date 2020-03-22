from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from app.formsubmit import bp
from app.formsubmit.forms import AddressForm
from werkzeug.urls import url_parse


@bp.route('/formredirect', methods=['GET', 'POST'])
def formredirect():
    # formredirect demonstrates how to accept form input from a user
    # The endpoint (/formredirect) accepts GET and POST requests
    # in order to present the blank form (GET) and validate a
    # submitted form (POST)

    # First, grab the form, which must be imported at the top of the
    # file.
    form = AddressForm()

    if form.validate_on_submit():
        # Should the request be a POST, the form must be validated.
        # The validate_on_submit() method will run the form's
        # validation that was specified in the form (I.e.
        # DataRequired)

        # Handle the next page
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        # Handle successful submission
        return redirect(next_page)

    # Get requests, as there won't be a form submission, will pass
    # the form into the renderer along with the template to be
    # displayed by the user's browser
    return render_template(
        'formsubmit/formredirect.html',
        form=form
    )
