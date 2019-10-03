from django.db import models


class SeawaterSample(models.Model):
    Other = "Other"
    sampleNumber = models.CharField(max_length=120)

    SURFACE = "Surface"
    BOTTOM = "Bottom"

    depthChoices = [
        (SURFACE, "Surface"),
        (BOTTOM, "Bottom")
    ]

    depth = models.CharField(
        max_length=7,
        choices=depthChoices,
        default=SURFACE
    )

    station18 = "18"
    stationA = "A"
    K6 = "K6"
    sampleLabel = models.CharField(max_length=120, blank=True)
    stationChoices = [
        (station18, "18"),
        (stationA, "A"),
        (K6, "K6"),
        (Other, "Other")
    ]
    sampleStation = models.CharField(
        max_length=2,
        choices=stationChoices,
        default=18
    )

    depth = models.CharField(
        max_length=7,
        choices=depthChoices,
        default=SURFACE
    )

    sampleGPS_N = models.CharField(max_length=25, blank=True)
    sampleGPS_E = models.CharField(max_length=25, blank=True)
    collectionTiming = models.DateTimeField(auto_now=False, blank=True)
    sampleVolume = models.FloatField(blank=True)
    sampleProcessed = models.BooleanField()

    RT = "Room Temperature"
    deg4 = "4 Degrees"
    mdeg20 = "-20 Degrees"
    mdeg80 = "-80 Degrees"

    storageChoices = [
        (RT, "Room Temperature"),
        (deg4, "4 Degrees Celsius"),
        (mdeg20, "Minus 20 Degrees Celsius"),
        (mdeg80, "Minus 80 Degrees Celsius")
    ]

    storage = models.CharField(
        max_length=20,
        choices=storageChoices,
        default=deg4
    )
    processedVolume = models.FloatField(blank=True)
    remainingVolume = models.FloatField(blank=True)

    qiagen = "Qiagen DNeasy Animal and Tissue Kit"
    MN = "Macherey-Nagel Nucleospin Kit"
    Mobio = "MO BIO PowerSoil DNA Isolation Kit"

    kitChoices = [(qiagen, "Qiagen DNeasy Animal and Tissue Kit"), (MN, "Macherey-Nagel Nucleospin Kit"),
                  (Mobio, "MO BIO PowerSoil DNA Isolation Kit"), (Other, "Other"), ]

    sampleKit = models.CharField(
        max_length=6,
        choices=kitChoices,
        default=qiagen
    )

    sampleDepth = models.FloatField(blank=True)
    sampleO2Level = models.FloatField(blank=True)
    sampleTemp = models.FloatField(blank=True)
    sampleSalinity = models.FloatField(blank=True)
    airTempInShade = models.FloatField(blank=True)
    cloudCover = models.CharField(max_length=120, blank=True)
    windSpeed = models.FloatField(blank=True)
    seaColor = models.CharField(max_length=120, blank=True)

    HTIDE = "htid"
    MTIDE = "mtid"
    LTIDE = "ltid"

    tideChoices = [
        (LTIDE, "Low Tide"),
        (MTIDE, "Mid Tide"),
        (HTIDE, "High Tide")
    ]

    tide = models.CharField(
        max_length=4,
        choices=tideChoices,
        default=LTIDE
    )

    RH = models.FloatField(blank=True)
    windDirection = models.CharField(max_length=2, blank=True)
    baromPressure = models.FloatField(blank=True)
    waveHeight = models.FloatField(blank=True)
    SucchiDisc = models.FloatField(blank=True)
    TotalDepth = models.FloatField(blank=True)
    Notes = models.TextField(blank=True)

    def __str__(self):
        return self.sampleLabel
