from worlds.LauncherComponents import Component, Type, components, launch, icon_paths

def run_client(*args: str) -> None:
    from .client.launch import launch_edf5_client
    
    launch(launch_edf5_client, name="EDF5 Client", args=args)
    
components.append(
    Component(
        "EDF5 Client",
        func=run_client,
        game_name="Earth Defense Force 5",
        component_type=Type.CLIENT,
        supports_uri=True,
        icon="EDF5",
    )
)

icon_paths["EDF5"] = f"ap:{__name__}/assets/icon.png"