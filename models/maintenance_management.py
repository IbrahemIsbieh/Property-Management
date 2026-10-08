from odoo import fields, models


class MaintenanceManagement(models.Model):
    _name = 'maintenance.management'
    _description = 'Maintenance Management'
    _inherit = ['mail.thread']

    # ---------------------------------------------------------
    # General Information
    # ---------------------------------------------------------

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
    # Maintenance Property
    # ---------------------------------------------------------

    home_property_id = fields.Many2one(
        'home.property',
        string='Property',
    )

    property_type = fields.Selection(
        related='home_property_id.property_type',
        string='Property Type',
        readonly=True,
    )

    owner_id = fields.Many2one(
        related='home_property_id.partner_id',
        string='Owner',
        readonly=True,
    )

    street = fields.Char(
        related='home_property_id.street',
        string='Street',
        readonly=True,
    )

    city = fields.Char(
        related='home_property_id.city',
        string='City',
        readonly=True,
    )

    area = fields.Float(
        related='home_property_id.area',
        string='Area',
        readonly=True,
    )

    notes = fields.Text(
        related='home_property_id.notes',
        string='Notes',
        readonly=True,
    )

    request_count = fields.Integer(
        related='home_property_id.request_count',
        string='Requests',
        readonly=True,
    )
