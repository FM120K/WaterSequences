from django.db import models


class SeawaterSample(models.Model):
    Other = "Other"
    SURFACE = "Surface"
    BOTTOM = "Bottom"

    depthChoices = [
        (SURFACE, "Surface"),
        (BOTTOM, "Bottom")
    ]
    station18 = "18"
    stationA = "A"
    K6 = "K6"
    stationChoices = [
        (station18, "18"),
        (stationA, "A"),
        (K6, "K6"),
        (Other, "Other")
    ]
    PR = "Processed"
    SFA = "Sent for Analysis"
    AR = "Analysis received"

    processedChoices = [
        (PR, "Processed"),
        (SFA, "Sent for Analysis"),
        (AR, "Analysis received")
    ]

    RT = "Room Temperature"
    deg4 = "4 Degrees Celsius"
    mdeg20 = "-20 Degrees Celsius"
    mdeg80 = "-80 Degrees Celsius"

    storageChoices = [
        (RT, "Room Temperature"),
        (deg4, "4 Degrees Celsius"),
        (mdeg20, "Minus 20 Degrees Celsius"),
        (mdeg80, "Minus 80 Degrees Celsius")
    ]

    qiagen = "Qiagen DNeasy Animal and Tissue Kit"
    MN = "Macherey-Nagel Nucleospin Kit"
    Mobio = "MO BIO PowerSoil DNA Isolation Kit"

    kitChoices = [(qiagen, "Qiagen DNeasy Animal and Tissue Kit"), (MN, "Macherey-Nagel Nucleospin Kit"),
                  (Mobio, "MO BIO PowerSoil DNA Isolation Kit"), (Other, "Other"), ]
                  

    HTIDE = "High Tide"
    MTIDE = "Mid Tide"
    LTIDE = "Low Tide"

    tideChoices = [
        (LTIDE, "Low Tide"),
        (MTIDE, "Mid Tide"),
        (HTIDE, "High Tide")
    ]
   
    sampleNumber = models.CharField(max_length=120)
    depth = models.CharField(
        max_length=50,
        choices=depthChoices,
        default=SURFACE
    )

    sampleLabel = models.CharField(max_length=120, blank=True)
    sampleStation = models.CharField(
        max_length=6,
        choices=stationChoices,
        default=18
    )

    sampleGPS_N = models.CharField(max_length=25, blank=True)
    sampleGPS_E = models.CharField(max_length=25, blank=True)

    sampleDate = models.TextField(max_length=25, blank=True)
    sampleTime = models.TextField(max_length=25, blank=True)
    
    sampleVolume = models.FloatField(blank=True, null = True)
    storage = models.CharField(
        max_length=20,
        choices=storageChoices,
        default=deg4
    )
    processed = models.CharField(
        max_length = 20,
        choices = processedChoices,
        default = PR
    )

    processedVolume = models.FloatField(null=True, blank=True)
    remainingVolume = models.FloatField(null=True, blank=True)

    extractionKit = models.CharField(
        max_length=120,
        choices=kitChoices,
        default=qiagen
    )

    sampleDepth = models.FloatField(blank=True, null=True)
    sampleO2Level = models.FloatField(blank=True, null=True)
    sampleTemp = models.FloatField(blank=True, null=True)
    sampleSalinity = models.FloatField(blank=True, null=True)
    airTempInShade = models.FloatField(blank=True, null=True)
    cloudCover = models.CharField(max_length=120, blank=True)
    windSpeed = models.FloatField(blank=True, null=True)
    seaColor = models.CharField(max_length=120, blank=True)

    tide = models.CharField(
        max_length=4,
        choices=tideChoices,
        default=LTIDE
    )

    RH = models.FloatField(blank=True, null= True)
    windDirection = models.CharField(max_length=2, blank=True)
    baromPressure = models.FloatField(blank=True, null = True)
    waveHeight = models.FloatField(blank=True, null= True)
    secchiDisk = models.FloatField(blank=True, null= True)
    TotalDepth = models.FloatField(blank=True, null= True)

    elutionVolume = models.FloatField(blank=True, null= True)
    Concentration = models.FloatField(blank=True, null= True)
    DNA_Concentration = models.FloatField(blank=True, null= True)
    Carb_Concentration = models.FloatField(blank=True, null= True)
    TotalYield = models.FloatField(blank=True, null= True)
    F_readfile = models.URLField(null=True, blank=True)
    R_readfile = models.URLField(null=True, blank=True)
    Notes = models.TextField(blank=True)

    def __str__(self):
        return self.sampleLabel
