class Room:
    def __init__(self, room_name, capacity, room_fee):
        self.room_name = room_name
        self.capacity = capacity
        self.guests = []
        self.songs = []
        self.room_fee = room_fee

    def guest_count(self):
        return len(self.guests)

    def check_in(self, guest_to_check_in):
        if self.capacity >= len([guest_to_check_in]):
            self.guests.append(guest_to_check_in)
            guest_to_check_in.guest_wallet -= self.room_fee
    
    def check_out(self, guest_to_check_out):
        self.guests.remove(guest_to_check_out)
    
    def song_count(self):
        return len(self.songs)
    
    def add_song_to_room(self, song_1):
        self.songs.append(song_1)

    