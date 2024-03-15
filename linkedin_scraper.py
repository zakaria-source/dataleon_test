from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurer le navigateur Selenium
# Il est recommandé d'utiliser des options de navigateur pour améliorer la performance et la discrétion
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')  # Exécute Chrome en mode headless si nécessaire
driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com")

# Pause pour simuler le comportement humain
time.sleep(2)

# Se connecter à LinkedIn
login_field = driver.find_element(By.ID, "session_key")
login_field.send_keys("zakaria-dbaba@hotmail.com")  # Remplacer par votre email
password_field = driver.find_element(By.ID, "session_password")
password_field.send_keys("Lebibliobus@10")  # Remplacer par votre mot de passe
password_field.send_keys(Keys.RETURN)

# Attendre que la page de profil soit chargée en utilisant WebDriverWait pour une meilleure fiabilité
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "global-nav")))

# Aller à la page des offres d'emploi
driver.get("https://www.linkedin.com/jobs")

# Attendre que la page des offres d'emploi soit chargée
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-box__text-input")))

# Pause pour simuler le comportement humain
time.sleep(3)

# Rechercher des emplois et postuler
job_title = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
job_title.send_keys("Développeur Python")

# Envoyer la recherche
job_title.send_keys(Keys.RETURN)

# Attendre que les résultats de recherche soient chargés
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card-container")))

# Trouver tous les éléments de poste
job_listings = driver.find_elements(By.CLASS_NAME, "job-card-container")

# Parcourir chaque poste et cliquer sur "Postuler" ou "Candidature simplifiée"
for job in job_listings:
    try:
        # Utiliser WebDriverWait pour attendre que le bouton soit cliquable
        apply_button = WebDriverWait(job, 2).until(
            EC.element_to_be_clickable(
                (By.XPATH, ".//button[contains(text(), 'Postuler') or contains(text(), 'Candidature simplifiée')]"))
        )
        apply_button.click()
        print("Postuler")
        # Ajouter ici la logique pour remplir et soumettre le formulaire de candidature si nécessaire
    except Exception as e:
        print("Pas de bouton de candidature trouvée pour ce poste ou erreur lors du clic : ", e)

# Fermer le navigateur une fois terminé
driver.quit()
