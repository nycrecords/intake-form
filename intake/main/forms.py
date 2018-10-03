from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, StringField, TextAreaField, FileField, SubmitField
from wtforms.fields.html5 import DateField, EmailField, TelField
from wtforms.validators import DataRequired, Optional

from .constants import DIVISIONS, PROJECT_TYPE, ENHANCEMENT, NEW_PROJECT, PRIORITY, PROJECT_ACCESS


class RequiredIf(DataRequired):
    """Validator which makes a field required if another field is set and has a truthy value.

    Sources:
        - http://wtforms.simplecodes.com/docs/1.0.1/validators.html
        - http://stackoverflow.com/questions/8463209/how-to-make-a-field-conditionally-optional-in-wtforms
        - https://gist.github.com/devxoul/7638142#file-wtf_required_if-py
    """
    field_flags = ('requiredif',)

    def __init__(self, message=None, *args, **kwargs):
        super(RequiredIf).__init__()
        self.message = message
        self.conditions = kwargs

    # field is requiring that name field in the form is data value in the form
    def __call__(self, form, field):
        for name, data in self.conditions.items():
            other_field = form[name]
            if other_field is None:
                raise Exception('no field named "%s" in form' % name)
            if other_field.data == data and not field.data:
                DataRequired.__call__(self, form, field)
            Optional()(form, field)


class IntakeForm(FlaskForm):
    """[summary]
    
    Args:
        FlaskForm ([type]): [description]
    """
    # Submission Information
    submitter_name = StringField('Submitter Name:', validators=[DataRequired()])
    submitter_email = EmailField('Submitter Email:', validators=[DataRequired()])
    submitter_phone = TelField('Submitter Phone:', validators=[DataRequired()])
    submitter_title = StringField('Submitter Title', validators=[DataRequired()])
    submitter_division = SelectField('Submitter Division:', choices=DIVISIONS, validators=[DataRequired()])

    # Project Information
    project_name = StringField('Name:', validators=[DataRequired()])
    enhancement_or_new_project = SelectField('Is this a new project or an enhancement to an existing project?', choices=PROJECT_TYPE, validators=[DataRequired()])
    current_project_name = StringField("If this is an enhancement, please provide the name of the current project:", validators=[RequiredIf(enhancement_or_new_project=ENHANCEMENT, message="You must provide the current project name if this is an enhancement")])
    project_background = TextAreaField("Background:", validators=[DataRequired()])
    project_goals = TextAreaField("Goals:", validators=[DataRequired()])
    priority = SelectField("Priority:", choices=PRIORITY, validators=[DataRequired()])
    completion_date = DateField("When do you want this project to be delivered?", validators=[DataRequired()])
    supplemental_materials_one = FileField("Supplemental Materials:")
    supplemental_materials_one_desc = StringField("Supplemental Materials Description: ", validators=[RequiredIf(supplemental_materials_one != "None")])
    supplemental_materials_two = FileField("Supplemental Materials")
    supplemental_materials_two_desc = StringField("Supplemental Materials Description: ", validators=[RequiredIf(supplemental_materials_two != None)])
    supplemental_materials_three = FileField("Supplemental Materials:")
    supplemental_materials_three_desc = StringField("Supplemental Materials Description: ", validators=[RequiredIf(supplemental_materials_three != None)])
    designated_business_owner_name = StringField('Designated Business Owner Name:', validators=[DataRequired()])
    designated_business_owner_email = EmailField('Designated Business Owner Email:', validators=[DataRequired()])
    designated_business_owner_phone = TelField('Designated Business Owner Phone:', validators=[DataRequired()])
    designated_business_owner_title = StringField('Designated Business Owner Title', validators=[DataRequired()])
    designated_business_owner_division = SelectField('Designated Business Owner Division:', choices=DIVISIONS, validators=[DataRequired()])

    # Technical Information
    project_access = SelectField("Who needs access to the final application?", choices=PROJECT_ACCESS, validators=[DataRequired()])
    login_required = BooleanField("Is login and account management functionality required?", validators=[DataRequired()])
    ui_ux_needed = BooleanField("Is UI / UX design needed?", validators=[DataRequired()])




    # Submit
    submit = SubmitField("Submit Intake Request")