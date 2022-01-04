# color_palette
Back-end developer competence test for COdesign

# What it does
1. Admin users can create colors using name and hex value
2. Authenticated users can create/edit/delete color palettes using colors and name the palettes. Palettes can be public or private.
3. Unauthenticated users can browse public palettes.
4. Authenticated users can save palettes to their favorites list.
5. Palettes can be searched by palette name or colors included in palette.

# Run project
    1. Clone repository
    2. Create virtual env in root. Python -m venv ./filename
    3. Run command ./venv/Scripts/activate.ps1(windows) to activate virtual environment.
    5. Go in to app directory ./colours
    6. Run command pip install -r requirements.txt to install dependencies.
    7. Run command python manage py migrate to set up database 
    8. Run command python manage.py createsuperuser to create superuser with username and password.
    9. Run command pyhton manage.py runserver to run project on localhost.


# API Endpoints

1. Auth

/auth/login/ (POST)
Parameters = [
    username=<string>
    password=<string>
]
Returns Token Key

/auth/logout/ (POST)

/auth/registration/ (POST)
Parameters = [
    username=<string>
    password1=<string>
    password2=<string>
    email=<string>
]
Returns Token Key

2. API

##
/api/colors/ (GET)
Returns list of all colors

/api/colors/create (POST) - restricted for Admin Users Only
Restriction = Admin users only
Parameters = {name=<string>, hex=<string>}

Pallette Object Sample = 
    {
        "id": 1,
        "history": [
            {
                "history_date": "2021-12-30T03:07:26.902142Z",
                "history_id": 1,
                "is_public": true,
                "last_edited": "2021-12-29T03:57:33.823621Z",
                "name": "test11",
                "primary_color1": 3,
                "primary_color2": 1,
                "secondary_color1": 2,
                "secondary_color2": 2,
                "secondary_color3": 5,
                "secondary_color4": 4
            }
        ],
        "primary_color1": "#808080",
        "primary_color2": "#000000",
        "secondary_color1": "#0000FF",
        "secondary_color2": "#0000FF",
        "secondary_color3": "#FF0000",
        "secondary_color4": "#FFFFFF",
        "is_public": true,
        "created": "2021-12-29T07:33:02.572666Z",
        "last_edited": "2021-12-29T03:57:33.823621Z",
        "name": "test11",
        "created_by": 1
    }

/api/palettes (GET) - unrestricted
Returns all palettes where palette.is_public==True
Type = List of Palette Objects

/api/palettes/?search=<str>
Returns all palettes where palette.is_public==True and 
    search string matches name of palette or the hex code of a color used in palette

api/user/palettes (GET, POST)
GET -> Returns all palettes created by current user including update history.
Type = List of Palette Objects
POST -> Create new palette with arguments = [
    primary_color1 = str(Color.hex),
    primary_color2 = str(Color.hex) required=false,
    secondary_color1 = str(Color.hex),
    secondary_color2 = str(Color.hex),
    secondary_color3 = str(Color.hex) required=false, 
    secondary_color4 = str(Color.hex) required=false,
    is_public = boolean
    name = string
] and sets current user for created_by field. Unique Constrained applied on colors.

/api/user/palettes/?is_public=<boolean>
Return all palettes where palettes.created_by is current user and palettes.is_public=arg

api/user/palettes/<str:name> (GET, PUT, PATCH, DELETE)
Performs GET, PUT, PATCH, DELETE on Palette object where obj.name=arg

api/user/favorites (GET)
Returns all Favorite objects(user, palette) where user is current user

api/user/save_palette/<str:name> (GET)
Gets Palettes with name=arg, if current user is in palette.saved_by, removes user from palette.saved_by, else adds user to palette.saved_by


# Afterthoughts

Need a csv upload option for colors

Should creating Color objects be available for all Authenticated Users? Hex values would need to be sanitized and validated.

Added name field to Colors but it might not be of any use. hex value enough should be sufficient. A color family OFreign Key would have been nice to group similar colors with.

Ideally primary colors and secondary colors in palettes should be two many2many fields with object count validation. Spent too much time trying too implement object count validation at the model level and went with individual Foreign Keys for each color option when time ran out. Validation can be implemented at view level or serializer level as well. I would change replace the 2 primary color Foreign Key fields and 4 secondary color Foreign Key Fields to 1 Primary Color Many2Many Field and one Secondary color Many2Many Field with Many2Many Field count validation on the Serializer if I could make another change to the project.

Should ideally use separate serializers for list views and detail views to make list fetch less expensive with larger databases.






