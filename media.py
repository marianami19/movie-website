import webbrowser
class Video():
    def __init__(self,video_name,duration,release_date):
        self.video_name=video_name
        self.video_duration=duration
        self.video_release_date=release_date

class Movie(Video):
    '''just some random movie trailers'''
    VALID_RATINGS=["G","PG","PG-13","R","NR","Approved","Disapproved"]#MY CLASS VARIABLE
    '''Under the Hays Code, films which seem to pre-date the current ratings system were simply approved or disapproved based on whether they were deemed "moral" or "immoral. '''
    def __init__(self,video_name,video_duration,video_release_date,storyline,poster,trailer,rating_num):
        Video.__init__(self,video_name,video_duration,video_release_date)
        self.movie_storyline=storyline
        self.movie_poster=poster
        self.movie_trailer=trailer
        self.rating_num=rating_num
    def show_trailer(self):
        '''opens browser to view movies trailer'''
        webbrowser.open(self.movie_trailer)
    def show_rating(self,VALID_RATINGS):
        '''returns the movie rating'''
        return VALID_RATINGS[self.rating_num]
