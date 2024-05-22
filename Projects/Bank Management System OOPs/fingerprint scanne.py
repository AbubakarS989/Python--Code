import dpfp
import dpfp.finger
import dpfp.io
import dpfp.processing


class FingerprintScanner:
    def __init__(self):
        self.reader = None
        self.fp_image = dpfp.io.Image()

    def initialize(self):
        self.reader = dpfp.pyfingerprint.Reader()

    def scan_fingerprint(self):
        try:
            if self.reader is None:
                raise ValueError("Fingerprint reader not initialized.")
            
            print("Place your finger on the scanner...")
            fingerprint_raw = self.reader.capture_fingerprint()
            fingerprint_image = dpfp.io.Image.fromstring(fingerprint_raw)
            self.fp_image.copy(fingerprint_image)

            print("Fingerprint scanned successfully.")
            return True
        except dpfp.pyfingerprint.FingerprintReaderError as e:
            print(f"Fingerprint scan failed: {e}")
            return False

class AuthenticationSystem:
    def __init__(self):
        self.scanner = FingerprintScanner()

    def authenticate(self):
        print("Welcome to the authentication system.")
        authenticated = False
        while not authenticated:
            if self.scanner.scan_fingerprint():
                print("Fingerprint scanned successfully.")
                # Logic to verify the scanned fingerprint against a database
                # For simplicity, we assume the fingerprint is always authenticated
                authenticated = True
                print("Authentication successful.")
            else:
                print("Fingerprint scan failed. Please try again.")

if __name__ == "__main__":
    auth_system = AuthenticationSystem()
    auth_system.scanner.initialize()
    auth_system.authenticate()
