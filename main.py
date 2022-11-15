import UI.cli as cli
import UI.api as api

should_use_api = True

if __name__ == '__main__':
    if should_use_api:
        api.app.run(debug=True)
    else:
        cli.main_menu()
