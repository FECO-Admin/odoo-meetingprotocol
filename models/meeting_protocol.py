from odoo import fields, models


class MeetingProtocol(models.Model):
    _name = "meeting.protocol"
    _description = "Meetingprotokoll"
    _rec_name = "title"
    _order = "date desc, id desc"

    title = fields.Char(string="Titel", required=True)
    date = fields.Datetime(
        string="Datum/Uhrzeit", default=fields.Datetime.now, required=True
    )
    duration_hours = fields.Float(string="Dauer (h)")
    location = fields.Char(string="Ort")
    participant_ids = fields.Many2many(
        "res.partner", string="Teilnehmer"
    )
    moderator_id = fields.Many2one(
        "res.partner", string="Moderator"
    )
    minutes_text = fields.Html(
        string="Protokoll",
        sanitize_attributes=False,
        strip_style=False,
    )
    state = fields.Selection(
        [
            ("draft", "Entwurf"),
            ("review", "In Prüfung"),
            ("final", "Freigegeben"),
        ],
        default="draft",
        string="Status",
    )
    agenda_ids = fields.One2many(
        "meeting.agenda.item",
        "protocol_id",
        string="Tagesordnung",
    )
    action_item_ids = fields.One2many(
        "meeting.action.item",
        "protocol_id",
        string="Aufgaben/Aktionen",
    )
    notes = fields.Text(string="Notizen")
    company_id = fields.Many2one(
        "res.company",
        string="Unternehmen",
        default=lambda self: self.env.company,
    )

    def action_draft(self):
        self.state = "draft"

    def action_review(self):
        self.state = "review"

    def action_final(self):
        self.write({"state": "final"})
