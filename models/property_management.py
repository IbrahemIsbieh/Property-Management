from odoo import fields, models


class PropertyManagement(models.Model):
    _name = 'property.management'
    _description = 'Property Management'
    _inherit = ['mail.thread']

    name = fields.Char(
        string='Management Name',
        required=True,
        tracking=True,
    )

    active = fields.Boolean(
        string='Active',
        default=True,
    )

    # ---------------------------------------------------------
    # Real Estate
    # ---------------------------------------------------------

    property_id = fields.Many2one(
        'property',
        string='Property',
    )

    property_ref = fields.Char(
        related='property_id.ref',
        string='Reference',
    )

    property_state = fields.Selection(
        related='property_id.state',
        string='State',
    )

    expected_price = fields.Float(
        related='property_id.expected_price',
        string='Expected Price',
    )

    selling_price = fields.Float(
        related='property_id.selling_price',
        string='Selling Price',
    )

    property_diff = fields.Float(
        related='property_id.diff',
        string='Difference',
    )

    bedroom = fields.Integer(
        related='property_id.bedroom',
        string='Bedrooms',
    )

    living_area = fields.Integer(
        related='property_id.living_area',
        string='Living Area',
    )

    garage = fields.Boolean(
        related='property_id.garage',
        string='Garage',
    )

    garden = fields.Boolean(
        related='property_id.garden',
        string='Garden',
    )

    garden_area = fields.Integer(
        related='property_id.garden_area',
        string='Garden Area',
    )

    facades = fields.Integer(
        related='property_id.facades',
        string='Facades',
    )

    owner_id = fields.Many2one(
        related='property_id.owner_id',
        string='Owner',
    )

    owner_phone = fields.Char(
        related='property_id.owner_phone',
        string='Owner Phone',
    )

    owner_address = fields.Char(
        related='property_id.owner_address',
        string='Owner Address',
    )