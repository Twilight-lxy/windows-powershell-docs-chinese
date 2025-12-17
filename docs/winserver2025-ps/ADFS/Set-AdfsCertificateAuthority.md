---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfscertificateauthority?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsCertificateAuthority
---

# 设置 AdfsCertificate Authority

## 摘要
修改证书颁发机构（CA）。

## 语法

### 自行签发（SelfIssued）
```
Set-AdfsCertificateAuthority [-SelfIssued] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RolloverSigningCertificate
```
Set-AdfsCertificateAuthority [-RolloverSigningCertificate] [-ForcePromotion] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### EnrollmentAgentConfiguration
```
Set-AdfsCertificateAuthority [-EnrollmentAgent] [-CertificateAuthority <String>]
 [-LogonCertificateTemplate <String>] [-WindowsHelloCertificateTemplate <String>]
 [-EnrollmentAgentCertificateTemplate <String>] [-AutoEnrollEnabled <Boolean>]
 [-CertificateGenerationThresholdDays <Int32>] [-WindowsHelloCertificateProxyEnabled <Boolean>] [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsCertificateAuthority` cmdlet 用于修改 Active Directory Federation Services (AD FS) 中的证书颁发机构（CA）。

## 示例

## 参数

### -AutoEnrollEnabled
{{填写自动注册功能的描述}}

```yaml
Type: Boolean
Parameter Sets: EnrollmentAgentConfiguration
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertificateAuthority
指定一个证书颁发机构（CA）。

```yaml
Type: String
Parameter Sets: EnrollmentAgentConfiguration
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertificateGenerationThresholdDays
请帮我填写 {{Fill CertificateGenerationThresholdDays Description}}

```yaml
Type: Int32
Parameter Sets: EnrollmentAgentConfiguration
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnrollmentAgent
```yaml
Type: SwitchParameter
Parameter Sets: EnrollmentAgentConfiguration
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnrollmentAgentCertificateTemplate
```yaml
Type: String
Parameter Sets: EnrollmentAgentConfiguration
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ForcePromotion
```yaml
Type: SwitchParameter
Parameter Sets: RolloverSigningCertificate
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogonCertificateTemplate
```yaml
Type: String
Parameter Sets: EnrollmentAgentConfiguration
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RolloverSigningCertificate
```yaml
Type: SwitchParameter
Parameter Sets: RolloverSigningCertificate
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SelfIssued
表示证书颁发机构是否是自行发行证书的（即该机构是否为自己生成了自己的证书）。

```yaml
Type: SwitchParameter
Parameter Sets: SelfIssued
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WindowsHelloCertificateProxyEnabled
{{填写 WindowsHelloCertificateProxyEnabled 的描述}}

```yaml
Type: Boolean
Parameter Sets: EnrollmentAgentConfiguration
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WindowsHelloCertificateTemplate
请帮我填写 {{Fill WindowsHelloCertificateTemplate Description}}

```yaml
Type: String
Parameter Sets: EnrollmentAgentConfiguration
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft IdentityServer.Management.Resources.AdfsCertificateAuthority

当指定*PassThru*参数时，该命令会返回更新后的AdfsCertificateAuthority对象。默认情况下，此cmdlet不会生成任何输出。

## 备注

## 相关链接

[禁用 AdfsCertificateAuthority](./ Disable-AdfsCertificateAuthority.md)

[Get-AdfsCertificateAuthority](./Get-AdfsCertificateAuthority.md)

