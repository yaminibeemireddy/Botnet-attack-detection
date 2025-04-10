import streamlit as st

def home_page():
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url('https://www.shutterstock.com/image-photo/system-hacked-warning-alert-on-600nw-2329841447.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-color: rgba(255, 255, 255, 0.6);
        background-blend-mode: overlay; 
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    profile_css = """
        <style>
            .transparent-box {
                background-color: rgba(255, 255, 255, 0.8);
                padding: 20px;
                border-radius: 20px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
                margin-bottom: 20px;
                font-family: Arial, sans-serif;
                border: 1px solid #e0e0e0;
            }
            .transparent1-box {
                background-color: rgba(255, 255, 255, 0.8);
                padding: 20px;
                border-radius: 20px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
                margin-bottom: 20px;
                font-family: Arial, sans-serif;
                border: 1px solid #e0e0e0;
            }
            .blue-header {
                font-size: 20px;
                font-weight: bold;
                color: blue;
                margin-bottom: 10px;
                text-align: center;
            }
            .red-header {
                font-size: 20px;
                font-weight: bold;
                color: red;
                margin-bottom: 10px;
                text-align: center;
            }
            .black-points {
                font-size: 14px;
                color: black;
                margin-left: 15px;
            }
            .full-width-blue-box {
                background-color: #d1ecf1;
                color: #0c5460;
                padding: 20px;
                border-radius: 10px;
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 20px;
                box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            }
        </style>
    """

    # HTML for the first transparent box
    transparent_box_html = f"""
        <div class="transparent-box">
            <div class="blue-header">What are Botnet Attacks?</div>
            <ul>
                <li class="black-points">A botnet is a network of infected devices.</li>
                <li class="black-points">Attackers use them for malicious purposes.</li>
                <li class="black-points">Examples include spam and DDoS attacks.</li>
                <li class="black-points">Botnets operate without user consent.</li>
            </ul>
        </div>
    """

    # HTML for the second full-width blue box
    full_width_blue_box_html = f"""
        <div class="full-width-blue-box">
            <strong>How It Works:</strong>
            Botnet attacks compromise devices by exploiting vulnerabilities, turning them into bots to perform tasks like spamming, stealing data or launching large-scale attacks.
        </div>
    """

    # Streamlit layout
    col1, col2 = st.columns([3, 3])

    # Column 1 content
    # Add the image
    col1.image(
        'https://cdni.iconscout.com/illustration/premium/thumb/iot-technology-illustration-download-in-svg-png-gif-file-formats--internet-things-smart-connection-artificial-intelligence-pack-network-communication-illustrations-10977231.png',
        use_column_width=True,
    )
    # Display the transparent box
    col2.markdown(profile_css + transparent_box_html, unsafe_allow_html=True)

    # Display the full-width blue box
    transparent_box_html = f"""
        <div class="transparent1-box">
            <div class="red-header">Applications of Botnet Attacks</div>
            <ul>
                <li class="black-points">Botnets can be used for various purposes.</li>
                <li class="black-points">They can be controlled remotely.</li>
                <li class="black-points">Botnets can be used to steal data.</li>
                <li class="black-points">They can be used to launch DDoS attacks.</li>
                <li class="black-points">Botnets can be used to send spam emails.</li>
                <li class="black-points">They can be used to mine cryptocurrency.</li>
                <li class="black-points">Botnets can be used to spread malware.</li>
                <li class="black-points">They can be used to launch ransomware attacks.</li>
                <li class="black-points">Botnets can be used to steal financial information.</li>
                <li class="black-points">They can be used to launch phishing attacks.</li>
            </ul>
        </div>
    """
    col2.markdown(full_width_blue_box_html, unsafe_allow_html=True)
    st.divider()
    col1,col2= st.columns([2,4])
    col2.video('https://www.youtube.com/watch?v=NbvBQRXL7WQ')
    col1.markdown(profile_css + transparent_box_html, unsafe_allow_html=True)
    st.divider()    