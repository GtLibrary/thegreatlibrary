using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

    public class ISO_CombatController : MonoBehaviour
    {
        #region VARIABLES
        private ISO_AnimationHandler AnimationHandler;
        [SerializeField] private float cooldownTime = 2f;
        private float nextFireTime = 0f;
        [SerializeField]private int noOfClicks = 0;
        private float lastClickedTime = 0;
        private float maxComboDelay = 1;
        #endregion

        #region UNITY METHODS

        private void Awake()
        {
            AnimationHandler = GetComponent<ISO_AnimationHandler>();
        }
        
        private void Update()
        {
 
            if (AnimationHandler._animator.GetCurrentAnimatorStateInfo(0).normalizedTime > 0.7f && AnimationHandler._animator.GetCurrentAnimatorStateInfo(0).IsName("ATK-1"))
            {
                AnimationHandler.SetATK1(false);
            }
            if (AnimationHandler._animator.GetCurrentAnimatorStateInfo(0).normalizedTime > 0.7f && AnimationHandler._animator.GetCurrentAnimatorStateInfo(0).IsName("ATK-2"))
            {
                AnimationHandler.SetATK2(false);
            }
            if (AnimationHandler._animator.GetCurrentAnimatorStateInfo(0).normalizedTime > 0.7f && AnimationHandler._animator.GetCurrentAnimatorStateInfo(0).IsName("ATK-3"))
            {
                AnimationHandler.SetATK3(false);
                noOfClicks = 0;
            }
 
 
            if (Time.time - lastClickedTime > maxComboDelay)
            {
                noOfClicks = 0;
            }
 
            //cooldown time
            if (Time.time > nextFireTime)
            {
                // Check for mouse input
                if (Input.GetMouseButtonDown(0))
                {
                    OnClick();
 
                }
            }
        }
        

        #endregion

        #region METHODS
        private void OnClick()
        {
            //so it looks at how many clicks have been made and if one animation has finished playing starts another one.
            lastClickedTime = Time.time;
            noOfClicks++;
            if (noOfClicks == 1)
            {
                AnimationHandler.SetATK1(true);
            }
            noOfClicks = Mathf.Clamp(noOfClicks, 0, 3);
 
            if (noOfClicks >= 2 && AnimationHandler._animator.GetCurrentAnimatorStateInfo(0).normalizedTime > 0.7f && AnimationHandler._animator.GetCurrentAnimatorStateInfo(0).IsName("ATK-1"))
            {
                AnimationHandler.SetATK1(false);
                AnimationHandler.SetATK2(true);
            }
            if (noOfClicks >= 3 && AnimationHandler._animator.GetCurrentAnimatorStateInfo(0).normalizedTime > 0.7f && AnimationHandler._animator.GetCurrentAnimatorStateInfo(0).IsName("ATK-2"))
            {
                AnimationHandler.SetATK2(false);
                AnimationHandler.SetATK3(true);
            }
        }

        #endregion
    }