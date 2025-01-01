# NeXus Neutron Data Reader 📊✨  

This repository provides tools for reading **NeXus neutron data** stored in HDF5 files using **TypeScript**, **JavaScript**, and **Python**. It includes examples, scripts, and a shell-based workflow for data exploration and analysis.

---

## Features ✨  

- **Multi-Language Support**: Implementations in TypeScript, JavaScript, and Python.  
- **HDF5 File Parsing**: Read and process NeXus-formatted neutron data.  
- **Shell Scripts**: Simplify installation and execution workflows.  
- **Dependency Management**: Use `yarn` for managing Node.js dependencies.  

---

## Prerequisites 🛠️  

- **Node.js** (14+ recommended)  
- **Python** (3.8+ recommended)  
- Required Python libraries:
  - `h5py`
  - `numpy`  
- `yarn` installed globally.  

---

## Installation  

1. Clone the repository:  
git clone https://github.com/your-username/nexus-data-reader.git  
cd nexus-data-reader  

2. Install Node.js dependencies:  
yarn install  

3. Install Python dependencies:  
pip install h5py numpy  

---

## Usage 🔧  

### JavaScript/TypeScript  

1. Read NeXus data with JavaScript:  
   node scripts/read_nexus.js <file.hdf5>  

2. Run the TypeScript implementation:  
   npx ts-node scripts/read_nexus.ts <file.hdf5>  

### Python  

1. Process NeXus data using the Python script:  
   python scripts/read_nexus.py <file.hdf5>  

### Shell Script  

1. Execute the shell script for end-to-end processing:  
   ./process_nexus.sh <file.hdf5>  

---

## File Structure 📂  

- `scripts/`: Contains implementations in JavaScript, TypeScript, and Python.  
- `process_nexus.sh`: Shell script for running the complete pipeline.  
- `README.md`: Documentation for the repository.  

---

## Example Commands  

- Node.js Implementation:  
  node scripts/read_nexus.js example.hdf5  

- Python Implementation:  
  python scripts/read_nexus.py example.hdf5  

- Shell Script:  
  ./process_nexus.sh example.hdf5  

---

## Contributing 🤝  

1. Fork the repository.  
2. Create a new branch:  
git checkout -b feature/your-feature  

3. Commit your changes:  
git commit -m "Add your feature"  

4. Push the branch:  
git push origin feature/your-feature  

5. Open a pull request.  

---

## License 📝  

This project is licensed under the MIT License. See the LICENSE file for details.  

---

**Easily explore NeXus neutron data with this multi-language reader!** 📊✨  
