class Talk:
    """A class for the talks."""
    def __init__(self,speaker,title,tags):
        self.speaker=speaker
        self.title=title
        self.tags=tags
        
    def get_speaker_firstname(self):
        return self.speaker.split()[0]
        
    def get_tags(self):
        return self.tags.split(',')
        
        
bdf1=Talk('govinda van Rossam','history python','python,history,c,advanced')
type(bdf1)
bdf1.get_speaker_firstname()
bdf1.get_tags()
 talk=Talk('Aurn K P','python bio','python bio')
 talk.get_speaker_firstname()
 talk.get_tags()
  talk.speaker='Aurn K p'
talk.tags='python boi'