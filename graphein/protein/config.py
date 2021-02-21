"""Base Config object for use with Protein Graph Construction"""
# Graphein
# Author: Arian Jamasb <arian@jamasb.io>
# License: MIT
# Project Website: https://github.com/a-r-j/graphein
# Code Repository: https://github.com/a-r-j/graphein
from __future__ import annotations

from pathlib import Path
from typing import Callable, List, Optional, Union

from pydantic import BaseModel

from graphein.protein.edges.intramolecular import peptide_bonds
from graphein.protein.features.nodes.amino_acid import meiler_embedding


class GetContactsConfig(BaseModel):
    """Config object for parameters relating to running GetContacts"""

    get_contacts_path: Path = Path(
        "/Users/arianjamasb/github/getcontacts/"
    ).resolve()
    contacts_dir: Path = Path("../examples/contacts/").resolve()
    pdb_dir: Path = Path("../examples/pdbs/").resolve()
    granularity: str = "CA"


class ProteinGraphConfig(BaseModel):
    """Config Object for Protein Structure Graph Construction"""

    granularity: str = "CA"
    keep_hets: bool = False
    insertions: bool = False
    pdb_dir: Path = Path(
        "../examples/pdbs/"
    )  # Also suggest to avoid hard-coding paths if possible!
    verbose: bool = True
    exclude_waters: bool = True
    covalent_bonds: bool = True
    include_ss: bool = True
    include_ligand: bool = False
    graph_constructor: Optional[str] = None
    verbose: bool = True
    deprotonate: bool = False
    long_interaction_threshold: Optional[int] = None
    protein_df_processing_functions: Optional[List[Callable]] = None
    edge_construction_functions: List[Union[Callable, str]] = [peptide_bonds]
    node_metadata_functions: Optional[List[Union[Callable, str]]] = [
        meiler_embedding
    ]
    edge_metadata_functions: Optional[List[Union[Callable, str]]] = None
    graph_metadata_functions: Optional[List[Callable]] = None
    get_contacts_config: Optional[GetContactsConfig] = GetContactsConfig()

    class Config:
        arbitrary_types_allowed: bool = True


class ProteinMeshConfig(BaseModel):
    """Config object for parameters relating to ProteinMeshConfig Mesh construction with PyMol"""

    pymol_command_line_options: Optional[str] = "-cKq"
    pymol_commands: Optional[List[str]] = ["show surface"]
