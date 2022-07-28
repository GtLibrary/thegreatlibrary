using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

    public class ISO_AnimationHandler : MonoBehaviour
    {
        #region VARIABLES

        public Animator _animator;
        
        private static readonly int IsMoving = Animator.StringToHash("isMoving");
        private static readonly int ATK1 = Animator.StringToHash("ATK-1");
        private static readonly int ATK2 = Animator.StringToHash("ATK-2");
        private static readonly int ATK3 = Animator.StringToHash("ATK-3");


        #endregion

        #region UNITY METHODS

        private void Awake()
        {
            _animator = GetComponent<Animator>();
        }

        #endregion

        #region METHODS

        public void SetIsMoving(bool value)
        {
            _animator.SetBool(IsMoving, value);
        }

        public void SetATK1(bool value)
        {
            _animator.SetBool(ATK1, value);
        }
        public void SetATK2(bool value)
        {
            _animator.SetBool(ATK2, value);
        }
        public void SetATK3(bool value)
        {
            _animator.SetBool(ATK3,value);
        }
        #endregion
    }