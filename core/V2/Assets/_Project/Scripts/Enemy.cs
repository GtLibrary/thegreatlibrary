using System;
using System.Collections;
using System.Collections.Generic;
using CodeMonkey.HealthSystemCM;
using UnityEngine;
using Random = UnityEngine.Random;


public class Enemy : MonoBehaviour, IGetHealthSystem
    {
        #region VARIABLES

        private Rigidbody _rgBody;
            //[SerializeField]private Material currentMat;
        [SerializeField] private Renderer thisRenderer;
        private Color prevColor;
        private Color newColor = Color.red;
        private HealthSystem m_HealthSystem;
        

        #endregion

        #region UNITY METHODS

        private void Awake()
        {
            _rgBody = GetComponent<Rigidbody>();
            m_HealthSystem = new HealthSystem(50f);
            m_HealthSystem.OnDead += HealthSystem_OnDead;
            // currentMat = GetComponent<Shader>();
        }


        private void OnCollisionEnter(Collision collision)
        {
            if (collision.collider.tag == "Fist")
            {
                Debug.Log("Ouch");
                StartCoroutine(Flash());
                Damage();

            }
        }

        #endregion

        #region METHODS

        private IEnumerator Flash()
        {
            thisRenderer.material.color = Color.red;
            yield return new WaitForSeconds(0.3f);
            thisRenderer.material.color = prevColor;
        }

        private void HealthSystem_OnDead(object sender, System.EventArgs e)
        {
            Destroy(gameObject);
        }
        private void Damage()
        {
            m_HealthSystem.Damage(10);
        }
        #endregion

        public HealthSystem GetHealthSystem()
        {
            return m_HealthSystem;
        }
    }