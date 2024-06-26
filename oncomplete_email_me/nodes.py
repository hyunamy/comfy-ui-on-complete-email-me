import smtplib
import re

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import comfy.utils

def is_valid_email(email):
    # Regular expression for validating an email address
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def send_gmail(sender_email, sender_password, recipient_emails, subject, body):

    # Check if sender email is valid
    if not is_valid_email(sender_email):
        print("Invalid sender email address.")
        return False

    # Convert recipient emails to a list, stripping whitespace and splitting by newline
    recipient_list = [email.strip() for email in recipient_emails.split('\n') if email.strip()]

    # Check if recipient emails are valid
    for recipient in recipient_list:
        if not is_valid_email(recipient):
            print(f"Invalid recipient email address: {recipient}")
            return False
        
    # SMTP server settings
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        # Connect to SMTP server and login
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()  # Identify yourself to the server
        server.starttls()  # Use TLS (Transport Layer Security)
        server.login(sender_email, sender_password)

        # Create the message
        message = f"Subject: {subject}\nMIME-Version: 1.0\nContent-Type: text/plain; charset=UTF-8\n\n{body}"

        # Send email to each recipient
        for recipient in recipient_list:
            server.sendmail(sender_email, recipient, message.encode('utf-8'))

        print("Email(s) sent successfully!")
        return True
    
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
    
    finally:
        # Close the server connection
        server.close()

class OnCompleteEmailMe:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.
    IS_CHANGED:
        optional method to control when the node is re executed.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "images": ("IMAGE", ),
                "sender_email": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "sender_email_address@gmail.com"
                }),
                "sender_password": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "input_type": "PASSWORD",
                    "default": "password"
                }),
                "recipient_emails": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "recipient_email1@gmail.com\nrecipient_email2@gmail.com",
                }),                
                "message": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Hello, this is a test email from ComfyUI!",
                }),
            },
        }

    RETURN_TYPES = ()

    FUNCTION = "on_complete_email_me"
    OUTPUT_NODE = True
    CATEGORY = "utils"

    def on_complete_email_me(self, images, sender_email, sender_password, recipient_emails, message):        
        pbar = comfy.utils.ProgressBar(images.shape[0])
        step = 0
        for image in images:
            pbar.update_absolute(step, images.shape[0])
            #when last image is processed, send email
            if step == images.shape[0]-1:
                subject = "ComfyUI OnComplete Email"
                body = message
                success = send_gmail(sender_email, sender_password, recipient_emails, subject, body)
            step += 1
        # Example usage
        print(f"Email sending success: {success}")
        return {}
    
    """
        The node will always be re executed if any of the inputs change but
        this method can be used to force the node to execute again even when the inputs don't change.
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        executed, if it is different the node will be executed again.
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        changes between executions the LoadImage node is executed again.
    """
    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""

# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
# WEB_DIRECTORY = "./somejs"

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "utils": OnCompleteEmailMe
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "utils": "OnCompleteEmailMe Prompts"
}
