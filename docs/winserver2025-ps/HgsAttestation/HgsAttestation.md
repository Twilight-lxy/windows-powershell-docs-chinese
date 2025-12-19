---
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.0.2
Locale: en-US
Module Guid: b0121942-ed2d-4a2b-959e-f0cfa64b48a9
Module Name: HgsAttestation
title: HgsAttestation
---

# HgsAttestation模块
## 描述
此参考资料提供了Host Guardian Service（HGS）认证相关cmdlet的描述和语法信息。这些cmdlet属于HgsAttestation模块。

## HgsAttestationCmdlets

### [Add-HgsAttestationCIPolicy](Add-HgsAttestationCIPolicy.md)
授权可信的代码完整性策略可供主机使用，以验证 HGS（硬件安全模块）的安全性。

### [Add-HgsAttestationDumpPolicy](Add-HgsAttestationDumpPolicy.md)
将一个授权的转储加密密钥添加到HGS中。

### [Add-HgsAttestationHostGroup](add-hgsattestationhostgroup.md)
为 Active Directory 主机组配置添加一个认证策略。

### [Add-HgsAttestationTpmHost](Add-HgsAttestationTpmHost.md)
将一台配备了TPM 2.0技术的受保护主机添加到HGS（Hardware Security Module）中的认证服务中。

### [Add-HgsAttestationTpmPolicy](Add-HgsAttestationTpmPolicy.md)
基于TPM 2.0硬件为HGS添加一个认证策略。

### [ Disable-HgsAttestationPolicy](Disable-HgsAttestationPolicy.md)
在 HGS 中禁用某个认证策略。

### [Enable-HgsAttestationPolicy](Enable-HgsAttestationPolicy.md)
在 HGS 中启用认证策略。

### [Get-HgsAttestationHostGroup](Get-HgsAttestationHostGroup.md)
根据主机组获取认证策略。

### [Get-HgsAttestationPolicy](Get-HgsAttestationPolicy.md)
获取 HGS 证明策略。

### [Get-HgsAttestationSignerCertificate](Get-HgsAttestationSignerCertificate.md)
获取用于签署认证证书的密钥对的公共证书。

### [Get-HgsAttestationTpmHost](Get-HgsAttestationTpmHost.md)
通过Attestation服务HGS来保护配备了TPM 2.0技术的主机。

### [Remove-HgsAttestationHostGroup](Remove-HgsAttestationHostGroup.md)
根据主机组删除某个认证策略。

### [Remove-HgsAttestationPolicy](Remove-HgsAttestationPolicy.md)
从HGS中删除一个证书颁发策略（attestation policy）。

### [Remove-HgsAttestationTpmHost](Remove-HgsAttestationTpmHost.md)
将配备了TPM 2.0技术的受保护主机从HGS（Hardware Security Module）的认证服务中移除。


