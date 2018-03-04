ART = 'artlogo.jpg'
ICON = 'icon-default.jpg'

NAME = 'Bay FM 99.9FM'
STREAM_URL = 'http://2bay.amrapstream.com:8000/stream'

####################################################################################################
def Start():

	ObjectContainer.art = R(ART)
	ObjectContainer.title1 = NAME
	TrackObject.thumb = R(ICON)

####################################################################################################     
@handler('/music/BayFM999', NAME, thumb=ICON, art=ART)
def MainMenu():

	oc = ObjectContainer()
	oc.add(CreateTrackObject(url=STREAM_URL, title=NAME))

	return oc

####################################################################################################
def CreateTrackObject(url, title, include_container=False):

	track_object = TrackObject(
		key = Callback(CreateTrackObject, url=url, title=title, include_container=True),
		rating_key = url,
		title = title,
		items = [
			MediaObject(
				parts = [
					PartObject(key=Callback(PlayAudio, url=url, ext='aac'))
				],
				container = Container.aac,
				bitrate = 128,
				audio_codec = AudioCodec.acc,
				audio_channels = 2
			)
		]
	)

	if include_container:
		return ObjectContainer(objects=[track_object])
	else:
		return track_object

####################################################################################################
def PlayAudio(url):

	return Redirect(url)
