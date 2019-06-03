import React, { Component } from "react";
import PropTypes from "prop-types";
import LOCALIZE from "../../text_resources";
import { loginAction, handleAuthResponseAndState } from "../../modules/LoginRedux";
import { connect } from "react-redux";
import history from "./history";

const styles = {
  loginContent: {
    padding: "12px 32px 0 32px",
    border: "1px solid #cdcdcd"
  },
  inputTitles: {
    padding: "12px 0 6px 0",
    fontWeight: "bold"
  },
  inputs: {
    width: "100%",
    padding: "3px 6px 3px 6px",
    border: "1px solid #00565E",
    borderRadius: 4
  },
  loginBtn: {
    width: 150,
    display: "block",
    margin: "24px auto"
  },
  loginError: {
    marginTop: 12,
    color: "#923534",
    fontWeight: "bold"
  },
  validationError: {
    color: "red",
    paddingTop: 8
  }
};

class LoginForm extends Component {
  static propTypes = {
    // Props from Redux
    loginAction: PropTypes.func,
    handleAuthResponseAndState: PropTypes.func,
    setLoginState: PropTypes.func,
    authenticated: PropTypes.bool
  };

  state = {
    username: "",
    password: "",
    wrongCredentials: false,
    passwordFieldAriaLabel: LOCALIZE.authentication.login.content.inputs.passwordTitle
  };

  // TODO(fnormand): encrypt passwords
  handleSubmit = event => {
    this.props
      .loginAction({ username: this.state.username, password: this.state.password })
      .then(response => {
        // credentials are wrong
        if (response.non_field_errors || typeof response.token === "undefined") {
          this.setState({
            wrongCredentials: true,
            passwordFieldAriaLabel:
              LOCALIZE.authentication.login.invalidCredentials +
              LOCALIZE.authentication.login.passwordFieldSelected
          });
          // focus on password field
          document.getElementById("password").focus();
          // right authentication
        } else {
          this.setState({ wrongCredentials: false });
          this.props.handleAuthResponseAndState(
            response,
            this.props.dispatch,
            window.location.pathname,
            history.push
          );
        }
      });
    event.preventDefault();
  };

  handleUsernameChange = event => {
    this.setState({ username: event.target.value });
  };

  handlePasswordChange = event => {
    this.setState({ password: event.target.value });
  };

  render() {
    return (
      <div>
        {!this.props.authenticated && (
          <div>
            <div style={styles.loginContent}>
              <h3>{LOCALIZE.authentication.login.content.title}</h3>
              <span>{LOCALIZE.authentication.login.content.description}</span>
              <form onSubmit={this.handleSubmit}>
                <div>
                  <div style={styles.inputTitles}>
                    <label htmlFor={"username"}>
                      {LOCALIZE.authentication.login.content.inputs.emailTitle}
                    </label>
                  </div>
                  <input
                    aria-label={LOCALIZE.authentication.login.content.inputs.emailTitle}
                    type="text"
                    placeholder={LOCALIZE.authentication.login.content.inputs.emailPlaceholder}
                    id="username"
                    style={styles.inputs}
                    onChange={this.handleUsernameChange}
                    value={this.state.username}
                  />
                </div>
                <div>
                  <div style={styles.inputTitles}>
                    <label htmlFor={"password"}>
                      {LOCALIZE.authentication.login.content.inputs.passwordTitle}
                    </label>
                  </div>
                  <input
                    aria-label={this.state.passwordFieldAriaLabel}
                    aria-invalid={this.state.wrongCredentials}
                    type="password"
                    placeholder={LOCALIZE.authentication.login.content.inputs.passwordPlaceholder}
                    id="password"
                    style={styles.inputs}
                    onChange={this.handlePasswordChange}
                    value={this.state.password}
                  />
                </div>
                <div>
                  {this.state.wrongCredentials && (
                    <label htmlFor={"password"} style={styles.loginError}>
                      {LOCALIZE.authentication.login.invalidCredentials}
                    </label>
                  )}
                </div>
                <input
                  style={styles.loginBtn}
                  className="btn btn-primary"
                  type="submit"
                  value={LOCALIZE.authentication.login.button}
                />
              </form>
            </div>
          </div>
        )}
      </div>
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  return {
    authenticated: state.login.authenticated
  };
};

const mapDispatchToProps = dispatch => ({
  loginAction: data => dispatch(loginAction(data)),
  handleAuthResponseAndState: (userData, dispatch, location, push) =>
    dispatch(handleAuthResponseAndState(userData, dispatch, location, push)),
  dispatch
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(LoginForm);
