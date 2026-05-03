// ================= INIT =================
document.addEventListener("DOMContentLoaded", () => {
    generateCaptcha("login");
    generateCaptcha("signup");
    generateCaptcha("forgot");

    setupNavigation();
    setupLogin();
});

// ================= CAPTCHA =================
let captchaStore = {};

function generateCaptcha(type) {
    const chars = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz23456789";
    let captcha = "";

    for (let i = 0; i < 5; i++) {
        captcha += chars.charAt(Math.floor(Math.random() * chars.length));
    }

    captchaStore[type] = captcha;

    const el = document.getElementById(type + "CaptchaText");
    if (el) el.textContent = captcha;
}

// ================= LOGIN =================
function setupLogin() {
    const form = document.getElementById("loginForm");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const email = document.getElementById("loginEmail").value;
        const password = document.getElementById("loginPassword").value;
        const captcha = document.getElementById("loginCaptchaInput").value;

        if (captcha !== captchaStore["login"]) {
            alert("Captcha wrong ❌");
            return;
        }

        try {
            const res = await fetch("/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email, password })
            });

            const data = await res.json();

            if (res.ok) {
                document.getElementById("authWrapper").style.display = "none";
                document.getElementById("dashboardWrapper").style.display = "flex";
            } else {
                alert(data.message || "Login failed");
            }
        } catch (err) {
            console.log(err);
        }
    });
}

// ================= NAVIGATION =================
function setupNavigation() {
    const navItems = document.querySelectorAll(".nav-item");

    navItems.forEach(btn => {
        btn.addEventListener("click", () => {
            if (btn.classList.contains("logout")) return;

            document.querySelectorAll(".nav-item").forEach(b => b.classList.remove("active"));
            btn.classList.add("active");

            const page = btn.getAttribute("data-page");

            document.querySelectorAll(".dash-section").forEach(sec => sec.classList.remove("active"));

            const sectionMap = {
                dashboard: "dashboardSection",
                learner: "learnerSection",
                verifier: "verifierSection",
                collaborator: "collaboratorSection",
                opportunity: "opportunitySection",
                reports: "reportsSection"
            };

            const section = document.getElementById(sectionMap[page]);
            if (section) section.classList.add("active");

            document.getElementById("pageTitle").innerText = btn.innerText;
        });
    });
}

// ================= LOGOUT =================
function handleLogout() {
    document.getElementById("dashboardWrapper").style.display = "none";
    document.getElementById("authWrapper").style.display = "block";
}

// ================= PASSWORD TOGGLE =================
function togglePass(id, btn) {
    const input = document.getElementById(id);
    input.type = input.type === "password" ? "text" : "password";
}

// ================= SEARCH =================
function openSearch() {
    document.getElementById("searchContainer").style.display = "flex";
}
function closeSearch() {
    document.getElementById("searchContainer").style.display = "none";
}

// ================= THEME =================
function toggleTheme() {
    document.body.classList.toggle("dark");
}

// ================= NOTIFICATIONS =================
function toggleNotifications() {
    document.getElementById("notificationDropdown").classList.toggle("show");
}
function markAllRead() {
    alert("All marked as read ✅");
}

// ================= OPPORTUNITY FIX =================
function openOpportunityModal() {
    alert("Add Opportunity clicked ✅");
}

// ================= VIEW DETAILS FIX =================
function openCourseDetails(name, data) {
    alert(`Course: ${name}\nEnrolled: ${data.enrolled}`);
}

// ================= COLLABORATOR =================
function openCollaboratorCourses(name) {
    alert("Opening courses for " + name);
}

// ================= VERIFIER =================
function openVerifierDetails(name) {
    alert("Verifier: " + name);
}

// ================= STUDENT FILTER =================
function filterStudents() {
    alert("Filtering students...");
}

// ================= VERIFIER FILTER =================
function filterVerifiers() {
    alert("Filtering verifiers...");
}

// ================= QUICK ADD =================
function openQuickAddModal() {
    alert("Quick Add Student");
}
function openBulkUploadModal() {
    alert("Bulk Upload");
}
function openQuickAddVerifierModal() {
    alert("Quick Add Verifier");
}
function openBulkUploadVerifierModal() {
    alert("Bulk Upload Verifier");
}