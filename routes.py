from flask import request, jsonify
from models import db, Admin, Opportunity
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


def init_routes(app):

    # ================= SIGNUP =================
    @app.route('/signup', methods=['POST'])
    @app.route('/api/signup', methods=['POST'])
    def signup():
        data = request.get_json()

        if Admin.query.filter_by(email=data.get('email')).first():
            return jsonify({"error": "Email already exists"}), 400

        user = Admin(
            full_name=data.get('full_name'),
            email=data.get('email'),
            password_hash=generate_password_hash(data.get('password'))
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "Signup success"}), 201


    # ================= LOGIN =================
    @app.route('/login', methods=['POST'])
    @app.route('/api/login', methods=['POST'])
    def login():
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        user = Admin.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({"error": "Invalid email or password"}), 401

        login_user(user)
        return jsonify({"message": "Login success"}), 200


    # ================= LOGOUT =================
    @app.route('/logout', methods=['POST'])
    @app.route('/api/logout', methods=['POST'])
    @login_required
    def logout():
        logout_user()
        return jsonify({"message": "Logged out"})


    # ================= FORGOT PASSWORD =================
    @app.route('/forgot-password', methods=['POST'])
    @app.route('/api/forgot-password', methods=['POST'])
    def forgot():
        return jsonify({"message": "If email exists, reset link sent"})


    # ================= CURRENT USER =================
    @app.route('/api/me', methods=['GET'])
    def get_current_user():
        if current_user.is_authenticated:
            return jsonify({
                "id": current_user.id,
                "email": current_user.email
            }), 200
        return jsonify({"error": "Not logged in"}), 401


    # ================= DASHBOARD DATA =================
    @app.route('/api/dashboard', methods=['GET'])
    @login_required
    def dashboard_data():
        total_ops = Opportunity.query.filter_by(admin_id=current_user.id).count()

        return jsonify({
            "total_opportunities": total_ops
        })


    # ================= GET OPPORTUNITIES =================
    @app.route('/opportunities', methods=['GET'])
    @app.route('/api/opportunities', methods=['GET'])
    @login_required
    def get_opportunities():
        ops = Opportunity.query.filter_by(admin_id=current_user.id).all()

        return jsonify([
            {
                "id": op.id,
                "name": op.name,
                "category": op.category,
                "duration": op.duration
            } for op in ops
        ])


    # ================= ADD =================
    @app.route('/opportunities', methods=['POST'])
    @app.route('/api/opportunities', methods=['POST'])
    @login_required
    def add_opportunity():
        data = request.get_json()

        op = Opportunity(
            name=data.get('name'),
            duration=data.get('duration'),
            category=data.get('category'),
            description=data.get('description'),
            admin_id=current_user.id
        )

        db.session.add(op)
        db.session.commit()

        return jsonify({"message": "Added"}), 201


    # ================= UPDATE =================
    @app.route('/opportunities/<int:id>', methods=['PUT'])
    @app.route('/api/opportunities/<int:id>', methods=['PUT'])
    @login_required
    def update_opportunity(id):
        op = Opportunity.query.get_or_404(id)

        if op.admin_id != current_user.id:
            return jsonify({"error": "Unauthorized"}), 403

        data = request.get_json()

        op.name = data.get('name')
        op.category = data.get('category')
        op.duration = data.get('duration')

        db.session.commit()

        return jsonify({"message": "Updated"})


    # ================= DELETE =================
    @app.route('/opportunities/<int:id>', methods=['DELETE'])
    @app.route('/api/opportunities/<int:id>', methods=['DELETE'])
    @login_required
    def delete_opportunity(id):
        op = Opportunity.query.get_or_404(id)

        if op.admin_id != current_user.id:
            return jsonify({"error": "Unauthorized"}), 403

        db.session.delete(op)
        db.session.commit()

        return jsonify({"message": "Deleted"})