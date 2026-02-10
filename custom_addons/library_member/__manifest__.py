{
    "name": "Library Member Management",
    "version": "17.0.1.0.0",
    "summary": "Manage library members and memberships",
    "description": "A beginner-friendly custom Odoo module to showcase Python and ORM basics.",
    "category": "Services",
    "author": "Your Name",
    "website": "https://github.com/yourusername/odoo",
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/library_member_views.xml",
        "data/library_member_sequence.xml",
    ],
    "application": True,
    "installable": True,
}
