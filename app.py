        @dataclass
class FamilyMember:
    relation: str
    occupation: str
    details: str

@dataclass
class StudentProfile:
    name: str = "Shreyas"
    standard: str = "Class 12th"
    stream: str = "Science"
    target_exams: List[str] = field(default_factory=lambda: ["12th Board Exams", "JEE (Joint Entrance Examination)"])
    
    # Coaching Information
    coaching_name: str = "Neha Tuition Classes"
    coaching_location: str = "Near Phunde Plot"
    
    # Family Details (Total 4 Members)
    family: List[FamilyMember] = field(default_factory=lambda: [
        FamilyMember("Father", "Private Job", "Working Professional"),
        FamilyMember("Mother", "Housewife", "Home Maker & Caretaker"),
        FamilyMember("Elder Brother", "Engineering Student", "Studying IT Branch at Government College of Engineering, Amravati"),
        FamilyMember("Self (Shreyas)", "Student", "Preparing for 12th Boards & JEE")
    ])
    
    # Best Friend Information
    best_friend_name: str = "Neha"
    best_friend_attributes: List[str] = field(default_factory=lambda: ["Very Good", "Caring", "Supportive", "Trustworthy"])

    def get_summary(self) -> Dict[str, str]:
        return {
            "Student": f"{self.name} ({self.standard} - {self.stream})",
            "Coaching": f"{self.coaching_name}, Location: {self.coaching_location}",
            "Brother Status": self.family[2].details,
            "Best Friend": f"{self.best_friend_name} (Qualities: {', '.join(self.best_friend_attributes)})"
        }

    def print_full_code_output(self) -> None:
        print("--- SHREYAS PROFILE DATA ---")
        for key, value in self.get_summary().items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    profile = StudentProfile()
    profile.print_full_code_output()
