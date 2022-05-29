class Room:
    def __init__(self, room_name, capacity):
        self.room_name = room_name
        self.capacity = capacity
        self.guests = []
        self.songs = []

    def guest_count(self):
        return len(self.guests)

    def check_in(self, guest_to_check_in):
        self.guests.append(guest_to_check_in)
    
    def check_out(self, guest_to_check_out):
        self.guests.remove(guest_to_check_out)
    
    def song_count(self):
        return len(self.songs)
    
    def add_song_to_room(self, song_1):
        self.songs.append(song_1)

    