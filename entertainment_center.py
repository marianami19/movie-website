import fresh_tomatoes
import media
clare_francis=media.Movie('Clare and Francis','3h 21m','7 October 2007','The life of St. Francis of Assisi and Clare, the bride of Christ.',"https://www.ignatius.com/Content/Site107/ProductImages/CF-M/265/Clare-and-Francis.jpg","https://www.youtube.com/watch?v=HtTLfQ0fwhI",4)
passion=media.Movie("Passion of Christ",'2h 7m','25 February 2004',"The passion and death of Lord Jesus.","https://images-na.ssl-images-amazon.com/images/M/MV5BNDY1N2IyYWMtZTY4OS00OGM1LTkxNmUtOTQzYmM5MmI2YmVmXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_QL50_.jpg","https://www.youtube.com/watch?v=4Aif1qEB_JU",3)
padre_pio=media.Movie("Padre Pio",'3h 22min ','17 April 2000',"The life of a poor Italian peasant boy Francesco who became Padre Pio","https://upload.wikimedia.org/wikipedia/en/thumb/5/5b/Padre_Pio_Miracle_Man.jpeg/250px-Padre_Pio_Miracle_Man.jpeg","https://www.youtube.com/watch?v=1_RvsYTF8Mo",4)
don_bosco=media.Movie("Don Bosco",'3h 20m','22 September 2004',"The life of Saint John Bosco and how he dedicated his life to rescuing abandoned and exploited street children in Turin.","https://upload.wikimedia.org/wikipedia/en/a/a0/Saint_John_Bosco-_Mission_to_Love.jpg","https://www.youtube.com/watch?v=Qs5aOa8xgtI",1)
david=media.Movie("Anthony: Warrior of God Trailer",'1h 50m',' 9 June 2006 ',"The life of Anthony of Padua, patron saint of lost things.","http://store.calvaryftl.org/images/products/9781400314058.jpg","https://www.youtube.com/watch?v=hZq9VWblEEY",4)
fatima=media.Movie("The Miracle of Our Lady of Fatima",'1h 42m','20 August 1952',"Our Lady appears to three children Lucia, Jacintha and Francesco.","https://upload.wikimedia.org/wikipedia/en/f/f5/The_Miracle_of_Our_Lady_of_Fatima_VHS_cover.jpg","https://www.youtube.com/watch?v=1jOFyznf53w",5)

movies=[clare_francis,passion,padre_pio,don_bosco,david,fatima]
fresh_tomatoes.open_movies_page(movies)
