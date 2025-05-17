 print(f"Erreur lors du chargement des données: {e}")
    print(traceback.format_exc())
    # Initialiser avec des valeurs par défaut pour éviter les erreurs au démarrage
    articles_info, index = None, None