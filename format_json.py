def format_json(title, category, link, thumbnail):
    json_contents = {
                        "embeds" : [
                            {
                                'title' : "Anime just aired!",
                                'color' : '8867816',

                                'footer' : {
                                    'text' : 'Created for AniManga | Delay up to 10 minutes'
                                },

                                'thumbnail' : {
                                    'url' : 'placeholder'
                                },

                                'fields' : [
                                    
                                        {
                                            "name": "Name",
                                            "value": "placeholder",
                                            "inline": True
                                        },

                                        {
                                            'name' : 'Type',
                                            'value' : 'placeholder',
                                            'inline' : True
                                        },

                                        {
                                            'name' : 'Info',
                                            'value' : 'placeholder',
                                            'inline' : False 
                                        }       
                                ]
                            }
                        ]
                    }

    json_contents['embeds'][0]['thumbnail']['url'] = thumbnail
    json_contents['embeds'][0]['fields'][0]['value'] = title
    json_contents['embeds'][0]['fields'][1]['value'] = category
    json_contents['embeds'][0]['fields'][2]['value'] = link

    return json_contents

#print(format_json('Sekai no Owari ni Shiba Inu to #71', 'OVA', 'https://www.livechart.me/anime/11327', "https://u.livechart.me/anime/11327/poster_image/cba70d91610220c61cbde0f213948fdc.webp?style=small&amp;format=jpg"))