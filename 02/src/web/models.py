from django.db import models


class Search(models.Model):
    day_name = models.CharField(
        verbose_name="Day (name)",
        max_length=100,
        choices=(
            ("Lunes", "Lunes"),
            ("Martes", "Martes"),
            ("Miércoles", "Miércoles"),
            ("Jueves", "Jueves"),
            ("Viernes", "Viernes"),
            ("Sábado", "Sábado"),
            ("Domingo", "Domingo"),
        ),
        blank=False,
    )
    enterprise = models.CharField(
        verbose_name="Enterprise",
        max_length=100,
        choices=(
            ("Grupo LATAM", "Grupo LATAM"),
            ("Sky Airline", "Sky Airline"),
            ("Aerolineas Argentinas", "Aerolineas Argentinas"),
            ("Copa Air", "Copa Air"),
            ("Latin American Wings", "Latin American Wings"),
            ("Avianca", "Avianca"),
            ("Gol Trans", "Gol Trans"),
            ("American Airlines", "American Airlines"),
            ("Air Canada", "Air Canada"),
            ("Delta Air", "Delta Air"),
            ("Iberia", "Iberia"),
            ("Air France", "Air France"),
            ("Aeromexico", "Aeromexico"),
            ("JetSmart SPA", "JetSmart SPA"),
            ("United Airlines", "United Airlines"),
            ("Alitalia", "Alitalia"),
            ("K.L.M.", "K.L.M."),
            ("British Airways", "British Airways"),
            ("Qantas Airways", "Qantas Airways"),
            ("Oceanair Linhas Aereas", "Oceanair Linhas Aereas"),
            ("Austral", "Austral"),
            ("Plus Ultra Lineas Aereas", "Plus Ultra Lineas Aereas"),
            ("Lacsa", "Lacsa"),
        ),
        blank=False,
    )
    month_name = models.CharField(
        verbose_name="Month",
        max_length=100,
        choices=(
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
            ("10", "10"),
            ("11", "11"),
            ("12", "12"),
        ),
        blank=False,
    )
    date_to_search = models.DateTimeField(
        verbose_name="Date",
        blank=False,
    )
    prediction = models.BooleanField(
        verbose_name="has delay",
        blank=True,
        null=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return str(self.id)
