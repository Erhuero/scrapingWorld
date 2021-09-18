describe("Login", function () {
    it('Sign in', function () {
        cy.visit('https://react-redux.realworld.io/#/login')
        cy.get('input[type="email"]').type('constantin.chtanko@gmail.com')
        cy.get('input[type="password"]').type('Osmium.222')
        cy.get('.btn').contains('Sign in').should('be.visibley').click()

            })
  })

