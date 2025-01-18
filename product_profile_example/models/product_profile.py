# © 2015 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductProfile(models.Model):
    _inherit = "product.profile"

    detailed_type = fields.Selection(
        selection_add=[("product", "Stockable Product")],
        ondelete={"product": "set default"},
    )

    sale_ok = fields.Boolean(
        string="Can be Sold",
        help="Specify if the product can be selected in a sales order line.",
    )
    purchase_ok = fields.Boolean(string="Can be Purchased")
    available_in_pos = fields.Boolean()
    profile_default_categ_id = fields.Many2one(
        "product.category", string="Default category", required=True
    )
