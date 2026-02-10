from odoo import api, fields, models
from odoo.exceptions import ValidationError


class LibraryMember(models.Model):
    _name = "library.member"
    _description = "Library Member"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "member_code"

    member_code = fields.Char(
        string="Member Code",
        readonly=True,
        copy=False,
        default=lambda self: "New",
        tracking=True,
    )
    name = fields.Char(required=True, tracking=True)
    email = fields.Char(required=True)
    phone = fields.Char()
    join_date = fields.Date(default=fields.Date.context_today, required=True)
    membership_type = fields.Selection(
        [("basic", "Basic"), ("premium", "Premium")],
        default="basic",
        required=True,
        tracking=True,
    )
    active = fields.Boolean(default=True)
    notes = fields.Text()

    @api.constrains("email")
    def _check_email_format(self):
        for record in self:
            if record.email and "@" not in record.email:
                raise ValidationError("Please provide a valid email address.")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("member_code", "New") == "New":
                vals["member_code"] = (
                    self.env["ir.sequence"].next_by_code("library.member") or "New"
                )
        return super().create(vals_list)
