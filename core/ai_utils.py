import re

CATEGORIES = [
    "Technique", "Sport", "Art", "Culture", "Entrepreneuriat", "Autre"
]

KEYWORDS_MAP = {
    "Technique": ["dev", "code", "python", "java", "web", "ai", "ia", "robot", "cyber", "data", "cloud"],
    "Sport": ["foot", "football", "basket", "tennis", "sport", "gym", "fitness", "run"],
    "Art": ["dessin", "peinture", "musique", "chant", "guitare", "théâtre", "photo", "cinéma"],
    "Culture": ["histoire", "culture", "langue", "club", "lecture", "débat", "ciné", "voyage"],
    "Entrepreneuriat": ["startup", "business", "marketing", "vente", "entreprise", "projet", "pitch"],
}

def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").lower()).strip()

def generate_event_description(titre: str, type_evenement: str, public_vise: str) -> str:
    titre = titre.strip()
    type_evenement = type_evenement.strip()
    public_vise = public_vise.strip()

    return (
        f"📌 {titre}\n\n"
        f"Cet événement est un(e) {type_evenement} conçu(e) pour {public_vise}. "
        f"Au programme : échanges, activités pratiques et moments de networking.\n\n"
        f"Vous y découvrirez des idées utiles, des conseils concrets et des exemples inspirants. "
        f"Rejoignez-nous pour apprendre, rencontrer de nouvelles personnes et vivre une expérience enrichissante.\n\n"
        f"✅ Places limitées — inscription obligatoire."
    )

def suggest_club_category(nom_club: str, description: str) -> str:
    text = normalize(nom_club) + " " + normalize(description)
    scores = {cat: 0 for cat in CATEGORIES}

    for cat, kws in KEYWORDS_MAP.items():
        for kw in kws:
            if kw in text:
                scores[cat] += 1

    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return "Autre"
    return best

def recommend_events(interests_keywords: str, events):
    keywords = [normalize(k) for k in interests_keywords.split(",") if normalize(k)]
    results = []

    for ev in events:
        haystack = normalize(ev.titre) + " " + normalize(ev.description)
        match_count = sum(1 for k in keywords if k in haystack)

        if match_count > 0:
            results.append((match_count, ev))

    results.sort(key=lambda x: x[0], reverse=True)
    top = results[:5]

    final = []
    for score, ev in top:
        justification = f"Correspond à {score} mot(s)-clé(s) de tes intérêts."
        final.append({"event": ev, "justification": justification})

    return final
