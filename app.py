from pathlib import Path

import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "pdfs" / "WK_resume.pdf"
swe_resume_file = current_dir / "pdfs" / "WK_SWE_resume.pdf"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Wynn"
PAGE_ICON = ":wave:"
NAME = "Wynn"
DESCRIPTION = """
Senior Computer Engineer Student at University of Michigan - Pursuing a Masters in CSE starting Fall 24
"""
EMAIL = "wynnkaza@umich.edu"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(swe_resume_file, "rb") as pdf_file:
    swe_PDFbyte = pdf_file.read()
with open("pdfs/EECS_373_Report.pdf", "rb") as pdf_file:
    eecs_373_report = pdf_file.read()
with open("pdfs/EECS_470_Report.pdf", "rb") as pdf_file:
    eecs_470_report = pdf_file.read()
with open("pdfs/EECS_583_Final_Report.pdf", "rb") as pdf_file:
    eecs_583_report = pdf_file.read()
with open("pdfs/EECS_587_Final_Report.pdf", "rb") as pdf_file:
    eecs_587_report = pdf_file.read()
with open("pdfs/EECS_570_Final_Report.pdf", "rb") as pdf_file:
    eecs_570_report = pdf_file.read()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st_lottie("https://lottie.host/94f8e07d-4f3e-4228-af43-28ea023f71aa/Pang0SoJZP.json", key="user")

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name="Wynn-Resume.pdf",
        mime="application/octet-stream",
    )
    st.download_button(
        label=" 📄 Download Resume",
        data=swe_PDFbyte,
        file_name="SWE-Wynn-Resume.pdf",
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    


# --- SOCIAL LINKS ---
st.write('\n')
col1, col2 = st.columns([2, 1], gap="small")
col1.write("📱[LinkedIn](https://www.linkedin.com/in/wynn-kaza/)")
col2.write("🗃️[GitHub](https://github.com/Fazanza)")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("About")
st.write(
    """
- ✔️ 3+ years experience working on software and hardware design
- ✔️ Interest in increasing software performance through hardware acceleration  
- ✔️ Excellent team-player and displays strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
- 👩‍💻 **Software**: C++, Python, GoLang, C, SQL
- 📚 **Software Libraries**: MPI, OpenMP, Cuda, LLVM
- ⚙️ **Hardware**: SystemVerilog / Verilog, ARM Assembly, Bash
- 💻 **Technology**: FPGA, Linux(Ubuntu), Altium/Allegro, Virtuoso, Version Contol(Git)
"""
)


# --- CourseWork ---
st.write("\n")
st.subheader("Course Work")
st.write(
    """
- 📟 Operating Systems, Parallel Computing, Advanced Compilers 
- 🌌 Parralel Computer Architecture, Computer Architecture, Computer Organization
- 🌠 Computer Networks, Digitally Integrated Circuits 
    """
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🤓", "**ENGR 100 Lab IA | UofM**")
st.write("01/2024 - 05/2024")
st.write(
    """
    - ► Instructed ENGR 100-250, An Introduction to Computing Systems with 70+ freshmen
    - ► Taught weekly lab sessions assisting students in Verilog to develop a single-cycle datapath processor on a FPGA
    - ► Hosted office hours to help in month long final project, focused on assembly and device drivers for IO devices
"""
)

# --- JOB 2
st.write("🚧", "**Hardware Developer Intern | IBM**")
st.write("05/2023 - 08/2023")
st.write(
    """
    - ► Revamped backend database infrastructure by transitioning from Sqlite3 to MariaDB
    - ► Designed Arduino Nano 33 BLE PCB shield and wrote API C++/Python library to interface between tester and computer
    - ► Refactored C++ code for vpd tools, increasing speed for future development and simplifying cross-platform compilation
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Electrical Engineering Intern | Whisker**")
st.write("05/2022 - 08/2022")
st.write(
    """
    - ► Developed a solution for Company’s Main Board Test Fixture, resolving an critical issue with the ESP-Programmer burning
        out when programming the main board
    - ► Constructed multiple R&D based PCBs in Altium, encapsulating breakout boards for ESP-Programmers, ToF Sensors, Stepper Motor Driver, and more
    - ► Built two test fixtures to test design changes on LR4 Main Board and ToF Board, verifying effect of board changes
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")

# -- Project 1
st.write('\n')
st.write("💻", "**R10K Inspired Out-of-Order Processor**")
st.write("10/2023 - 12/2023")
st.write("""
        - ► Design and implementing N-Way Superscalar OoO processor with Early Branch Resolution with RISC-V ISA support using
            SystemVerilog
        - ► Developed Pag branch predictor, non-blocking D-Cache, victim cache, and Store-To-Load Forwarding to improve CPI
        - ► Synthesized design obtained 12.06 ns clock period with a 1.87 CPI average on test bench
""")
st.download_button(
        label=" 📄 Download Report",
        data=eecs_470_report,
        file_name="OoO-Processor-Report.pdf",
        mime="application/octet-stream",
)

# -- Project 2
st.write('\n')
st.write("💻", "**CPU-GPU Heterogeneous System Simulator for Coherence Performance")
st.write("2/2024 - 5/2024")
st.write("""
        - ► Design and implemented system simulator for heterogenous CPU-GPU architecture to simulate coherence performance
        - ► Implemented the Spandex Protocol for LLC to handle communication between CPU MSI and GPU VI coherence protocol
        - ► Was able to effectively simulate effect of different cache parameters and network delay on the cycle count
""")
st.download_button(
        label=" 📄 Download Report",
        data=eecs_570_report,
        file_name="System-Simulator-Report.pdf",
        mime="application/octet-stream",
)

# -- Project 3
st.write('\n')
st.write("🐉", "**Cache Tiling and Tile Size Selection Algorithms**")
st.write("10/2023 - 12/2023")
st.write("""
        - ► Wrote LLVM pass to replicate cache tiling to reduce number of cache misses in matrix multiplication
        - ► Improved upon original tiling algorithm by reducing instruction overhead (specifically branches)
        - ► Developed two new algorithms to find optimal tiling size within the new restrictions: implemented algorithms obtained
            58.56% and 84.37% less cache miss than the original untiled matrix multiplication
""")
st.download_button(
        label=" 📄 Download Report",
        data=eecs_583_report,
        file_name="Cache-Tiling-Report.pdf",
        mime="application/octet-stream",
)

# -- Project 4
st.write('\n')
st.write("🤯", "**DP Parallelization in OpenMP**")
st.write("10/2023 - 01/2024")
st.write("""
        - ► Reworked original GoLang algorithm for solving the Dictionary Problem in C++
        - ► Developed a OpenMP Parallization solution for running the algorithm which obtained
         a speedup of 1.2 times on four cores compared to the original algorithm

""")
st.download_button(
        label=" 📄 Download Report",
        data=eecs_587_report,
        file_name="DP_Parallelization.pdf",
        mime="application/octet-stream",
)