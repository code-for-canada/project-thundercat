import React, { Component } from "react";
import PropTypes from "prop-types";
import LOCALIZE from "../../text_resources";
import validateName, { validateEmail, validatePassword } from "../../helpers/regexValidator";
import "../../css/registration-form.css";
import { registerAction } from "../../modules/LoginRedux";
import { bindActionCreators } from "redux";
import { connect } from "react-redux";
import PopupBox, { BUTTON_TYPE } from "../commons/PopupBox";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCheckCircle } from "@fortawesome/free-solid-svg-icons";

const styles = {
  createAccountContent: {
    padding: "12px 32px 0 32px",
    border: "1px solid #cdcdcd"
  },
  inputTitle: {
    padding: "12px 0 6px 0",
    fontWeight: "bold"
  },
  inputs: {
    width: "100%",
    padding: "3px 6px 3px 6px",
    borderRadius: 4
  },
  inputForNames: {
    width: 240,
    padding: "3px 6px 3px 6px",
    borderRadius: 4
  },
  dobFields: {
    width: 40,
    padding: "3px 6px 3px 6px",
    borderRadius: 4,
    textAlign: "center",
    marginRight: 12
  },
  iconForNames: {
    color: "#278400",
    position: "absolute",
    margin: "8px 0 0 220px"
  },
  iconForOtherFields: {
    color: "#278400",
    position: "absolute",
    margin: "8px 0 0 484px"
  },
  loginBtn: {
    width: 150,
    display: "block",
    margin: "24px auto"
  },
  passwordRequirementsError: {
    color: "#923534",
    marginTop: 6,
    fontWeight: "bold"
  },
  errorMessage: {
    color: "#923534",
    fontWeight: "bold",
    padding: 0,
    marginTop: 6
  },
  mandatoryMark: {
    color: "#923534"
  }
};

const MANDATORY_MARK = " *";

class RegistrationForm extends Component {
  static propTypes = {
    // Props from Redux
    registerAction: PropTypes.func
  };

  state = {
    // Ensures no errors are shown on page load
    isFirstLoad: true,
    // Form content and validation
    firstNameContent: "",
    isValidFirstName: false,
    lastNameContent: "",
    isValidLastName: false,
    dobDayContent: "",
    isValidDobDay: false,
    dobMonthContent: "",
    isValidDobMonth: false,
    dobYearContent: "",
    isValidDobYear: false,
    emailContent: "",
    isValidEmail: false,
    passwordContent: "",
    isValidPassword: false,
    isFirstPasswordLoad: true,
    passwordConfirmationContent: "",
    isValidPasswordConfirmation: false,
    // PopupBox
    showDialog: false,
    // handle errors
    accountExistsError: false
  };

  getFirstNameContent = event => {
    const firstNameContent = event.target.value;
    this.setState({
      firstNameContent: firstNameContent
    });
  };

  getLastNameContent = event => {
    const lastNameContent = event.target.value;
    this.setState({
      lastNameContent: lastNameContent
    });
  };

  getDobDayContent = event => {
    const dobDayContent = event.target.value;
    const regex = /^(3[01]|[12][0-9]|[1-9])$/;
    if (event.target.value === "" || regex.test(event.target.value)) {
      this.setState({
        dobDayContent: dobDayContent
      });
    }
  };

  getDobMonthContent = event => {
    const dobMonthContent = event.target.value;
    const regex = /^(1[0-2]|[1-9])$/;
    if (event.target.value === "" || regex.test(event.target.value)) {
      this.setState({
        dobMonthContent: dobMonthContent
      });
    }
  };

  getDobYearContent = event => {
    const dobYearContent = event.target.value;
    const regex = /^[0-9]$/;
    if (event.target.value === "" || regex.test(event.target.value)) {
      this.setState({
        dobYearContent: dobYearContent
      });
    }
  };

  getEmailContent = event => {
    const emailContent = event.target.value;
    this.setState({ emailContent: emailContent });
  };

  getPasswordContent = event => {
    const passwordContent = event.target.value;
    this.setState({
      passwordContent: passwordContent
    });
  };

  getPasswordConfirmationContent = event => {
    const passwordConfirmationContent = event.target.value;
    this.setState({
      passwordConfirmationContent: passwordConfirmationContent
    });
  };

  validateForm = () => {
    const isValidFirstName = validateName(this.state.firstNameContent);
    const isValidLastName = validateName(this.state.lastNameContent);
    const isValidDobDay = this.state.dobDayContent.length > 0;
    const isValidDobMonth = this.state.dobMonthContent.length > 0;
    const isValidDobYear = this.state.dobYearContent.length > 0;
    const isValidEmail = validateEmail(this.state.emailContent);
    const isValidPassword = validatePassword(this.state.passwordContent);
    const passwordContent = this.state.passwordContent;
    const passwordConfirmationContent = this.state.passwordConfirmationContent;
    this.setState({
      isFirstLoad: false,
      isFirstPasswordLoad: false,
      accountExistsError: false,
      isValidFirstName: isValidFirstName,
      isValidLastName: isValidLastName,
      isValidDobDay: isValidDobDay,
      isValidDobMonth: isValidDobMonth,
      isValidDobYear: isValidDobYear,
      isValidEmail: isValidEmail,
      isValidPassword: isValidPassword,
      isValidPasswordConfirmation: passwordContent === passwordConfirmationContent
    });
  };

  // checks if all fields are valid
  isFormValid = () => {
    return (
      this.state.isValidFirstName &&
      this.state.isValidLastName &&
      this.state.isValidEmail &&
      this.state.isValidPassword &&
      this.state.isValidPasswordConfirmation
    );
  };

  redirectToLoginPage = () => {
    // refresh the page in order to show the login form
    window.location.reload();
    // close dialog
    this.setState({ showDialog: false });
  };

  handleSubmit = event => {
    const validForm = this.isFormValid();
    // if all fields are valid, execute API errors validation
    if (validForm) {
      this.props
        .registerAction({
          username: this.state.emailContent,
          email: this.state.emailContent,
          password: this.state.passwordContent
        })
        // API errors validation
        .then(response => {
          // account already exists
          if (response.username[0] === "A user with that username already exists.") {
            this.setState({ accountExistsError: true });
            // focus on email address field
            document.getElementById("email-address-field").focus();
            // account successfully created
          } else {
            this.setState({ showDialog: true, accountExistsError: false });
          }
        });
    }
    event.preventDefault();
  };

  render() {
    const {
      isFirstLoad,
      firstNameContent,
      isValidFirstName,
      lastNameContent,
      isValidLastName,
      dobDayContent,
      isValidDobDay,
      dobMonthContent,
      isValidDobMonth,
      dobYearContent,
      isValidDobYear,
      emailContent,
      isValidEmail,
      passwordContent,
      isValidPassword,
      isFirstPasswordLoad,
      passwordConfirmationContent,
      isValidPasswordConfirmation,
      accountExistsError
    } = this.state;

    const validFieldClass = "valid-field";
    const invalidFieldClass = "invalid-field";

    return (
      <div>
        <div>
          <div style={styles.createAccountContent}>
            <h3>{LOCALIZE.authentication.createAccount.content.title}</h3>
            <span>{LOCALIZE.authentication.createAccount.content.description}</span>
            <form onSubmit={this.handleSubmit}>
              <div className="names-grid">
                <div className="names-grid-first-name">
                  <div style={styles.inputTitle}>
                    <label htmlFor={"first-name-field"}>
                      {LOCALIZE.authentication.createAccount.content.inputs.firstNameTitle}
                    </label>
                    <span style={styles.mandatoryMark}>{MANDATORY_MARK}</span>
                  </div>
                  {isValidFirstName && (
                    <FontAwesomeIcon style={styles.iconForNames} icon={faCheckCircle} />
                  )}

                  <input
                    className={
                      isValidFirstName || isFirstLoad ? validFieldClass : invalidFieldClass
                    }
                    aria-invalid={!this.state.isValidFirstName && !isFirstLoad}
                    aria-required={"true"}
                    id="first-name-field"
                    type="text"
                    value={firstNameContent}
                    style={styles.inputForNames}
                    onChange={this.getFirstNameContent}
                  />
                  {!isValidFirstName && !isFirstLoad && (
                    <label htmlFor={"first-name-field"} style={styles.errorMessage}>
                      {LOCALIZE.authentication.createAccount.content.inputs.firstNameError}
                    </label>
                  )}
                </div>
                <div className="names-grid-last-name">
                  <div style={styles.inputTitle}>
                    <label htmlFor={"last-name-field"}>
                      {LOCALIZE.authentication.createAccount.content.inputs.lastNameTitle}
                    </label>
                    <span style={styles.mandatoryMark}>{MANDATORY_MARK}</span>
                  </div>
                  {isValidLastName && (
                    <FontAwesomeIcon style={styles.iconForNames} icon={faCheckCircle} />
                  )}
                  <input
                    className={isValidLastName || isFirstLoad ? validFieldClass : invalidFieldClass}
                    aria-invalid={!this.state.isValidLastName && !isFirstLoad}
                    aria-required={"true"}
                    id="last-name-field"
                    type="text"
                    value={lastNameContent}
                    style={styles.inputForNames}
                    onChange={this.getLastNameContent}
                  />
                  {!isValidLastName && !isFirstLoad && (
                    <label htmlFor={"last-name-field"} style={styles.errorMessage}>
                      {LOCALIZE.authentication.createAccount.content.inputs.lastNameError}
                    </label>
                  )}
                </div>
              </div>
              <div>
                <div style={styles.inputTitle}>
                  <label>{LOCALIZE.authentication.createAccount.content.inputs.dobDayTitle}</label>
                  <span style={styles.mandatoryMark}>{MANDATORY_MARK}</span>
                </div>
                <input
                  className={isValidDobDay || isFirstLoad ? validFieldClass : invalidFieldClass}
                  aria-required={"true"}
                  id="dob-day-field"
                  value={dobDayContent}
                  style={styles.dobFields}
                  onChange={this.getDobDayContent}
                />
                <input
                  className={isValidDobMonth || isFirstLoad ? validFieldClass : invalidFieldClass}
                  aria-required={"true"}
                  id="dob-month-field"
                  value={dobMonthContent}
                  style={styles.dobFields}
                  onChange={this.getDobMonthContent}
                />
                <input
                  className={isValidDobYear || isFirstLoad ? validFieldClass : invalidFieldClass}
                  aria-required={"true"}
                  id="dob-year-field"
                  value={dobYearContent}
                  style={styles.dobFields}
                  onChange={this.getDobYearContent}
                />
                {!(isValidDobDay && isValidDobMonth && isValidDobYear) && !isFirstLoad && (
                  <div>
                    <label htmlFor={"dob-day-field"} style={styles.errorMessage}>
                      {LOCALIZE.authentication.createAccount.content.inputs.dobError}
                    </label>
                  </div>
                )}
              </div>
              <div>
                <div style={styles.inputTitle}>
                  <label htmlFor={"email-address-field"}>
                    {LOCALIZE.authentication.createAccount.content.inputs.emailTitle}
                  </label>
                  <span style={styles.mandatoryMark}>{MANDATORY_MARK}</span>
                </div>
                {isValidEmail && (
                  <FontAwesomeIcon style={styles.iconForOtherFields} icon={faCheckCircle} />
                )}
                <input
                  className={isValidEmail || isFirstLoad ? validFieldClass : invalidFieldClass}
                  aria-invalid={!this.state.isValidEmail && !isFirstLoad}
                  aria-required={"true"}
                  id="email-address-field"
                  type="text"
                  value={emailContent}
                  style={styles.inputs}
                  onChange={this.getEmailContent}
                />
                {!isValidEmail && !isFirstLoad && (
                  <label htmlFor={"email-address-field"} style={styles.errorMessage}>
                    {LOCALIZE.authentication.createAccount.content.inputs.emailError}
                  </label>
                )}
              </div>
              {accountExistsError && (
                <label htmlFor={"email-address-field"} style={styles.errorMessage}>
                  {LOCALIZE.authentication.createAccount.accountAlreadyExistsError}
                </label>
              )}
              <div>
                <div style={styles.inputTitle}>
                  <label htmlFor={"password-field"}>
                    {LOCALIZE.authentication.createAccount.content.inputs.passwordTitle}
                  </label>
                  <span style={styles.mandatoryMark}>{MANDATORY_MARK}</span>
                </div>
                {isValidPassword && (
                  <FontAwesomeIcon style={styles.iconForOtherFields} icon={faCheckCircle} />
                )}
                <input
                  className={isValidPassword || isFirstLoad ? validFieldClass : invalidFieldClass}
                  aria-invalid={!isValidPassword && !isFirstLoad}
                  aria-required={"true"}
                  id="password-field"
                  type="password"
                  value={passwordContent}
                  style={styles.inputs}
                  onChange={this.getPasswordContent}
                />
                {!isValidPassword && !isFirstPasswordLoad && (
                  <label htmlFor={"password-field"}>
                    <p style={styles.errorMessage}>
                      {
                        LOCALIZE.authentication.createAccount.content.inputs.passwordErrors
                          .description
                      }
                    </p>
                    <ul style={styles.passwordRequirementsError}>
                      <li>
                        {
                          LOCALIZE.authentication.createAccount.content.inputs.passwordErrors
                            .upperCase
                        }
                      </li>
                      <li>
                        {
                          LOCALIZE.authentication.createAccount.content.inputs.passwordErrors
                            .lowerCase
                        }
                      </li>
                      <li>
                        {LOCALIZE.authentication.createAccount.content.inputs.passwordErrors.digit}
                      </li>
                      <li>
                        {
                          LOCALIZE.authentication.createAccount.content.inputs.passwordErrors
                            .specialCharacter
                        }
                      </li>
                      <li>
                        {LOCALIZE.authentication.createAccount.content.inputs.passwordErrors.length}
                      </li>
                    </ul>
                  </label>
                )}
              </div>
              <div>
                <div style={styles.inputTitle}>
                  <label htmlFor={"password-confirmation-field"}>
                    {LOCALIZE.authentication.createAccount.content.inputs.passwordConfirmationTitle}
                  </label>
                  <span style={styles.mandatoryMark}>{MANDATORY_MARK}</span>
                </div>
                {isValidPasswordConfirmation && (
                  <FontAwesomeIcon style={styles.iconForOtherFields} icon={faCheckCircle} />
                )}
                <input
                  className={
                    isValidPasswordConfirmation || isFirstLoad ? validFieldClass : invalidFieldClass
                  }
                  aria-invalid={!isValidPasswordConfirmation && !isFirstLoad}
                  aria-required={"true"}
                  id="password-confirmation-field"
                  type="password"
                  value={passwordConfirmationContent}
                  style={styles.inputs}
                  onChange={this.getPasswordConfirmationContent}
                />
                {!isValidPasswordConfirmation && !isFirstPasswordLoad && (
                  <label htmlFor={"password-confirmation-field"} style={styles.errorMessage}>
                    {LOCALIZE.authentication.createAccount.content.inputs.passwordConfirmationError}
                  </label>
                )}
              </div>
              <button
                style={styles.loginBtn}
                className="btn btn-primary"
                type="submit"
                onClick={this.validateForm}
              >
                {LOCALIZE.authentication.createAccount.button}
              </button>
            </form>
          </div>
        </div>
        <PopupBox
          isCloseButtonVisible={false}
          isBackdropStatic={true}
          show={this.state.showDialog}
          handleClose={this.redirectToLoginPage}
          title={LOCALIZE.authentication.createAccount.popupBox.title}
          description={
            <div>
              <p>{LOCALIZE.authentication.createAccount.popupBox.description}</p>
            </div>
          }
          rightButtonType={BUTTON_TYPE.primary}
          rightButtonTitle={LOCALIZE.commons.ok}
          rightButtonAction={this.redirectToLoginPage}
        />
      </div>
    );
  }
}

const mapDispatchToProps = dispatch =>
  bindActionCreators(
    {
      registerAction
    },
    dispatch
  );

export default connect(
  null,
  mapDispatchToProps
)(RegistrationForm);
