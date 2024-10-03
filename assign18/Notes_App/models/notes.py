class Notes:
    user_id: int
    note: str
    created_at: int

    def __init__(self, user_id: int, note: str, created_at: int):
        self.user_id = user_id
        self.note = note
        self.created_at = created_at

    def __str__(self):
        return f"{self.user_id} {self.note} {self.created_at}"
    
    def __repr__(self):
        return str(self)
    
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "note": self.note,
            "created_at": self.created_at
        }
    