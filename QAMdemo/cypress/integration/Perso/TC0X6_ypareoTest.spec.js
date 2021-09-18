describe("Login", function () {
    it('Sign in', function () {
        cy.visit('https://ypareo.formation-aftec.com/')
        cy.get('input[id="login"]').type('cchtanko')
        cy.get('input[id="password"]').type('Osmium.222')
        cy.get('.btn').contains('Se connecter').should('be.visible').click()

            })
  })
