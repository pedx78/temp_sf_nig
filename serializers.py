from app import ma

from historic_model import Historical

class HistoricalSchema(ma.ModelSchema):
    class Meta:
        model = Historical

h_schema = HistoricalSchema()
