import re

modifier_path = r'e:\LOGICIELS\OUTIL POTAGER\potager\modifier-semence.html'
repertoire_path = r'e:\LOGICIELS\OUTIL POTAGER\potager\repertoire.html'
fiche_path = r'e:\LOGICIELS\OUTIL POTAGER\potager\fiche-semence.html'

html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Gérer la fiche - Potager 2026</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" type="image/png" href="https://raw.githubusercontent.com/frugman/potager/main/favicon.png">
</head>
<body>
    <header>
        <a href="#" onclick="window.history.length > 1 ? window.history.back() : window.location.href='repertoire.html'; return false;" class="back-btn">←</a>
        <h1 id="page-title">Nouvelle Semence</h1>
    </header>

    <div class="container">
        <form id="editForm" onsubmit="event.preventDefault(); save();">
            <div class="card">
                <div class="note-meta">1. Identité de la plante</div>
                
                <label>Nom commun</label>
                <input type="text" id="nom_commun" required placeholder="Ex: Tomate">

                <label>Variété</label>
                <input type="text" id="variete" required placeholder="Ex: Noire de Crimée">

                <div class="grid-2">
                    <div>
                        <label>Famille</label>
                        <select id="famille">
                            <option value="">Sélectionnez...</option>
                            <option value="Solanacées">🍅 Solanacées (Tomate...)</option>
                            <option value="Cucurbitacées">🥒 Cucurbitacées (Courge...)</option>
                            <option value="Fabacées">🫘 Fabacées (Haricot...)</option>
                            <option value="Brassicacées">🥦 Brassicacées (Chou...)</option>
                            <option value="Alliacées">🧅 Alliacées (Ail, Oignon...)</option>
                            <option value="Apiacées">🥕 Apiacées (Carotte...)</option>
                            <option value="Astéracées">🌼 Astéracées (Laitue...)</option>
                            <option value="Chénopodiacées">🥬 Chénopodiacées (Bette...)</option>
                            <option value="Lamiacées">🌿 Lamiacées (Basilic...)</option>
                            <option value="Autre">Autre</option>
                        </select>
                    </div>
                    <div>
                        <label>Provenance</label>
                        <input type="text" id="provenance" placeholder="Ex: Kokopelli">
                    </div>
                </div>

                <div class="grid-2">
                    <div>
                        <label>Durée Germinative</label>
                        <select id="duree_germ">
                            <option value="">Inconnue</option>
                            <option value="1">1 an</option>
                            <option value="2">2 ans</option>
                            <option value="3">3 ans</option>
                            <option value="4">4 ans</option>
                            <option value="5">5+ ans</option>
                        </select>
                    </div>
                    <div>
                        <label>Associations</label>
                        <input type="text" id="associes" placeholder="Bonnes/Mauvaises">
                    </div>
                </div>

                <label>Description / Notes</label>
                <textarea id="description" rows="2" placeholder="Informations générales..."></textarea>
            </div>

            <div class="card">
                <div class="note-meta">2. Conseils de Culture</div>
                
                <div class="grid-2">
                    <div>
                        <label>Exposition</label>
                        <select id="exposition">
                            <option value="Soleil">☀️ Plein Soleil</option>
                            <option value="Mi-ombre">⛅ Mi-ombre</option>
                            <option value="Ombre">☁️ Ombre</option>
                        </select>
                    </div>
                    <div>
                        <label>Arrosage</label>
                        <select id="eau">
                            <option value="Normal">💧 Normal</option>
                            <option value="Faible">🌵 Faible</option>
                            <option value="Important">💧💧 Important</option>
                        </select>
                    </div>
                </div>

                <div class="grid-2">
                    <div>
                        <label>Style de semis</label>
                        <select id="style_semis">
                            <option value="Godet puis terre">🪴 Godet d'abord</option>
                            <option value="En poquet">🤏 En poquet</option>
                            <option value="En ligne claire">➖ Ligne claire</option>
                            <option value="À la volée">🌪️ À la volée</option>
                        </select>
                    </div>
                    <div>
                        <label>Profondeur</label>
                        <select id="profondeur">
                            <option value="1cm">1 cm</option>
                            <option value="2cm">2 cm</option>
                            <option value="3cm">3 cm</option>
                            <option value="4cm">4+ cm</option>
                            <option value="En surface">Surface</option>
                        </select>
                    </div>
                </div>

                <div class="grid-2">
                    <div>
                        <label>Dist. entre plants</label>
                        <input type="number" id="dist_rang" placeholder="Ex: 30 cm">
                    </div>
                    <div>
                        <label>Dist. entre rangs</label>
                        <input type="number" id="dist_inter" placeholder="Ex: 50 cm">
                    </div>
                </div>

                <div class="grid-2">
                    <div>
                        <label>Temp. Levée Maxi</label>
                        <input type="text" id="temp_levee" placeholder="Ex: 18°C">
                    </div>
                    <div>
                        <label>Période de semis (Mois)</label>
                        <input type="text" id="periode_semis" placeholder="Mars, Avril...">
                    </div>
                </div>
            </div>

            <div class="card">
                <div class="note-meta">3. Moteur Agenda (Délais en jours)</div>
                <p style="font-size: 11px; color: var(--text-secondary); margin-bottom: 15px;">
                    Indispensable pour calculer les dates de repiquage, plantation et récolte.
                </p>
                
                <div class="grid-2">
                    <div>
                        <label>Levée</label>
                        <input type="number" id="d_levee" required>
                    </div>
                    <div>
                        <label>Repiquage</label>
                        <input type="number" id="d_repiquage">
                    </div>
                </div>
                <div class="grid-2">
                    <div>
                        <label>Plantation</label>
                        <input type="number" id="d_plantation">
                    </div>
                    <div>
                        <label>Maturité</label>
                        <input type="number" id="d_maturite">
                    </div>
                </div>
            </div>

            <div class="card">
                <div class="note-meta">4. Tâches Récurrentes (L'Ampoule 💡)</div>
                <p style="font-size: 11px; color: var(--text-secondary); margin-bottom: 15px;">
                    Programmez ici les soins automatiques qui s'ajouteront à l'agenda (Taille, Butter...).
                    Règles : Ébourgeonner, Pincer, Butter, etc. généreront l'ampoule du lexique.
                </p>
                
                <div id="tasks-container"></div>
                
                <button type="button" class="filter-btn" style="margin-top:10px; border-style: dashed; width:100%;" onclick="addTask()">
                    ➕ AJOUTER UNE TÂCHE
                </button>
            </div>

            <button type="submit" class="save-btn" id="btnSave">
                SAUVEGARDER
            </button>
        </form>
    </div>

    <script>
        const id = new URLSearchParams(window.location.search).get('id');
        const user = localStorage.getItem('gh_user'), repo = localStorage.getItem('gh_repo'), token = localStorage.getItem('gh_token');
        let currentSha = "";
        let existingSeeds = [];

        async function load() {
            if(!token) { window.location.href = 'parametres.html'; return; }
            if(id) { document.getElementById('page-title').innerText = "Gérer la Fiche"; }

            try {
                const res = await fetch(`https://api.github.com/repos/${user}/${repo}/contents/semences.json?t=${Date.now()}`, { 
                    headers: { 'Authorization': `Bearer ${token}` } 
                });
                const data = await res.json();
                currentSha = data.sha;
                existingSeeds = JSON.parse(decodeURIComponent(escape(atob(data.content))));
                
                if(id) {
                    const s = existingSeeds.find(item => String(item.id) === String(id));
                    if(s) {
                        document.getElementById('nom_commun').value = s.identite?.nom_commun || "";
                        document.getElementById('variete').value = s.identite?.variete || "";
                        document.getElementById('famille').value = s.identite?.famille || "";
                        document.getElementById('provenance').value = s.identite?.provenance || "";
                        document.getElementById('duree_germ').value = s.identite?.duree_germ || "";
                        document.getElementById('description').value = s.identite?.description || "";
                        document.getElementById('associes').value = s.particularites?.associes || "";
                        
                        document.getElementById('exposition').value = s.culture?.exposition || s.technique?.exposition || "Soleil";
                        document.getElementById('eau').value = s.culture?.eau || s.technique?.eau || "Normal";
                        document.getElementById('style_semis').value = s.culture?.style_semis || "Godet puis terre";
                        document.getElementById('profondeur').value = s.culture?.profondeur || "1cm";
                        document.getElementById('temp_levee').value = s.culture?.temp_levee || "";
                        document.getElementById('dist_rang').value = s.culture?.dist_rang || s.technique?.distance || "";
                        document.getElementById('dist_inter').value = s.culture?.dist_inter || "";
                        document.getElementById('periode_semis').value = (s.culture?.periode_semis || []).join(", ");
                        
                        document.getElementById('d_levee').value = s.delais?.levee || 0;
                        document.getElementById('d_repiquage').value = s.delais?.repiquage || 0;
                        document.getElementById('d_plantation').value = s.delais?.plantation || 0;
                        document.getElementById('d_maturite').value = s.delais?.maturite || 0;

                        if(s.taches_entretien) {
                            s.taches_entretien.forEach(t => addTask(t.label, t.delai, t.base, t.frequence, t.occurences));
                        }
                    }
                } else {
                    // Nouvel ajout = 1 tâche par défaut pour aider
                    addTask("Arroser", 2, "plantation", 7, 5); 
                }
            } catch(e) { console.error(e); }
        }

        function addTask(label = "", delai = 0, base = "semis", frequence = 0, occurences = 1) {
            const container = document.getElementById('tasks-container');
            const div = document.createElement('div');
            div.style.padding = "15px";
            div.style.background = "rgba(255,255,255,0.02)";
            div.style.borderRadius = "12px";
            div.style.border = "1px solid var(--border-color)";
            div.style.marginBottom = "10px";
            div.style.position = "relative";
            
            div.innerHTML = `
                <div style="position:absolute; right:10px; top:10px; color:var(--danger-red); font-weight:bold; cursor:pointer;" onclick="this.parentElement.remove()">✕</div>
                <label>Libellé de la tâche</label>
                <select class="t-label">
                    <option value="Arroser" ${label==='Arroser'?'selected':''}>Arroser 💧</option>
                    <option value="Taille / Pincement" ${label==='Taille / Pincement'?'selected':''}>Taille / Pincer ✂️</option>
                    <option value="Ébourgeonner" ${label==='Ébourgeonner'?'selected':''}>Ébourgeonner (Gourmands) ✂️</option>
                    <option value="Butter" ${label==='Butter'?'selected':''}>Butter ⛏️</option>
                    <option value="Biner" ${label==='Biner'?'selected':''}>Biner ⛏️</option>
                    <option value="Pailler" ${label==='Pailler'?'selected':''}>Pailler</option>
                    <option value="Diriger" ${label==='Diriger'?'selected':''}>Diriger / Palisser 🌿</option>
                    <option value="Éclaircir" ${label==='Éclaircir'?'selected':''}>Éclaircir ✂️</option>
                    <option value="Nettoyer les fleurs fanées" ${label==='Nettoyer les fleurs fanées'?'selected':''}>Nettoyer les fleurs fanées</option>
                    <option value="${label}" ${!['Arroser','Taille / Pincement','Ébourgeonner','Butter','Biner','Pailler','Diriger','Éclaircir','Nettoyer les fleurs fanées'].includes(label)?'selected':''}>${!['Arroser','Taille / Pincement','Ébourgeonner','Butter','Biner','Pailler','Diriger','Éclaircir','Nettoyer les fleurs fanées'].includes(label)?label:'Autre (Libre)'}</option>
                </select>
                <input type="text" class="t-custom" value="${!['Arroser','Taille / Pincement','Ébourgeonner','Butter','Biner','Pailler','Diriger','Éclaircir','Nettoyer les fleurs fanées'].includes(label)?label:''}" placeholder="Si Autre, écrivez ici" style="margin-top:5px;">
                
                <div class="grid-2" style="margin-top: 15px;">
                    <div>
                        <label>Délai initial (j)</label>
                        <input type="number" class="t-delai" value="${delai}">
                    </div>
                    <div>
                        <label>Référence</label>
                        <select class="t-base">
                            <option value="semis" ${base==='semis'?'selected':''}>Après semis</option>
                            <option value="plantation" ${base==='plantation'?'selected':''}>Après plant.</option>
                            <option value="levee" ${base==='levee'?'selected':''}>Après levée</option>
                        </select>
                    </div>
                </div>
                <div class="grid-2">
                    <div>
                        <label>Répéter tous les (j)</label>
                        <input type="number" class="t-freq" value="${frequence}" placeholder="0 = non">
                    </div>
                    <div>
                        <label>Nb. de fois max</label>
                        <input type="number" class="t-occ" value="${occurences}" placeholder="1 = ponctuel">
                    </div>
                </div>
            `;
            container.appendChild(div);
        }

        function generateSlug(nom, variete) {
            let str = (nom + " " + variete).toLowerCase();
            str = str.normalize("NFD").replace(/[\u0300-\u036f]/g, ""); 
            str = str.replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, ""); 
            return str || "semence-inconnue";
        }

        async function save() {
            const btn = document.getElementById('btnSave'); 
            btn.innerText = "⏳ SYNCHRONISATION..."; btn.disabled = true;

            try {
                // Tâches
                const tasks = [];
                document.querySelectorAll('#tasks-container > div').forEach(el => {
                    let label = el.querySelector('.t-label').value;
                    if(label.startsWith('Autre') || (el.querySelector('.t-custom').value !== "")) label = el.querySelector('.t-custom').value;
                    if(label) {
                        tasks.push({
                            label: label,
                            delai: parseInt(el.querySelector('.t-delai').value) || 0,
                            base: el.querySelector('.t-base').value,
                            frequence: parseInt(el.querySelector('.t-freq').value) || 0,
                            occurences: parseInt(el.querySelector('.t-occ').value) || 1
                        });
                    }
                });

                // Périodes
                const periodesText = document.getElementById('periode_semis').value;
                const periodes = periodesText ? periodesText.split(',').map(s=>s.trim()).filter(Boolean) : [];

                const seedData = {
                    identite: {
                        nom_commun: document.getElementById('nom_commun').value,
                        variete: document.getElementById('variete').value,
                        famille: document.getElementById('famille').value,
                        provenance: document.getElementById('provenance').value,
                        duree_germ: document.getElementById('duree_germ').value,
                        description: document.getElementById('description').value
                    },
                    particularites: {
                        associes: document.getElementById('associes').value
                    },
                    culture: {
                        exposition: document.getElementById('exposition').value,
                        eau: document.getElementById('eau').value,
                        style_semis: document.getElementById('style_semis').value,
                        profondeur: document.getElementById('profondeur').value,
                        temp_levee: document.getElementById('temp_levee').value,
                        dist_rang: parseInt(document.getElementById('dist_rang').value) || "",
                        dist_inter: parseInt(document.getElementById('dist_inter').value) || "",
                        periode_semis: periodes
                    },
                    delais: {
                        levee: parseInt(document.getElementById('d_levee').value) || 0,
                        repiquage: parseInt(document.getElementById('d_repiquage').value) || 0,
                        plantation: parseInt(document.getElementById('d_plantation').value) || 0,
                        maturite: parseInt(document.getElementById('d_maturite').value) || 0
                    },
                    taches_entretien: tasks
                };

                let seeds = existingSeeds;
                let finalId = id;

                if(id) {
                    const index = seeds.findIndex(s => String(s.id) === String(id));
                    if(index !== -1) {
                        // Conserver les vieux attributs non modifiables ici
                        seedData.conseil_semis = seeds[index].conseil_semis;
                        seeds[index] = { ...seeds[index], ...seedData };
                    }
                } else {
                    let baseId = generateSlug(seedData.identite.nom_commun, seedData.identite.variete);
                    finalId = baseId;
                    let count = 1;
                    while (seeds.some(s => s.id === finalId)) {
                        finalId = `${baseId}-${count}`;
                        count++;
                    }
                    seedData.id = finalId;
                    seeds.push(seedData);
                }

                await fetch(`https://api.github.com/repos/${user}/${repo}/contents/semences.json`, {
                    method: 'PUT', headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        message: id ? `Etape 14: Modification globale de la semence ${finalId}` : `Etape 14: Ajout de semence hybride ${finalId}`,
                        content: btoa(unescape(encodeURIComponent(JSON.stringify(seeds, null, 2)))),
                        sha: currentSha
                    })
                });

                window.location.href = `fiche-semence.html?id=${finalId}`;
            } catch(e) {
                console.error(e);
                alert("Erreur de sauvegarde !");
                btn.innerText = "SAUVEGARDER"; btn.disabled = false;
            }
        }

        window.onload = load;
    </script>
</body>
</html>
"""

with open(modifier_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Update repertoire.html and fiche-semence.html
with open(repertoire_path, "r", encoding="utf-8") as f:
    rep = f.read()
rep = rep.replace('href="ajout-semence.html"', 'href="modifier-semence.html"')
with open(repertoire_path, "w", encoding="utf-8") as f:
    f.write(rep)

with open(fiche_path, "r", encoding="utf-8") as f:
    fiche = f.read()
fiche = fiche.replace('href=`ajout-semence.html?edit=${seedId}`', 'href=`modifier-semence.html?id=${seedId}`')
with open(fiche_path, "w", encoding="utf-8") as f:
    f.write(fiche)

print("done")
