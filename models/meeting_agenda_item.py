from odoo import fields, models


class MeetingAgendaItem(models.Model):
    _name = "meeting.agenda.item"
    _description = "Tagesordnungspunkt"
    _order = "sequence, id"

    protocol_id = fields.Many2one(
        "meeting.protocol",
        string="Protokoll",
        required=True,
        ondelete="cascade",
    )
    sequence = fields.Integer(string="Reihenfolge", default=10)
    title = fields.Char(string="Punkt", required=True)
    presenter_id = fields.Many2one("res.partner", string="Vortragender")
    duration_minutes = fields.Integer(string="Dauer (Min.)")
    notes = fields.Html(string="Ergebnis/Besprechung")
