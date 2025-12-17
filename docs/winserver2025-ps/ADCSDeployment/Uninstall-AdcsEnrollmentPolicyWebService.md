---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Deployment.Commands.dll-Help.xml
Module Name: ADCSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsdeployment/uninstall-adcsenrollmentpolicywebservice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Uninstall-AdcsEnrollmentPolicyWebService
---

# 卸载 AdcsEnrollmentPolicyWebService

## 摘要
卸载“证书注册策略”Web服务。

## 语法

### UninstallSingleInstance（默认设置）

```
Uninstall-AdcsEnrollmentPolicyWebService -AuthenticationType <AuthenticationType>
 [-KeyBasedRenewal] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### UninstallAll

```
Uninstall-AdcsEnrollmentPolicyWebService [-AllPolicyServers] [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Uninstall-AdcsEnrollmentPolicyWebService` cmdlet 用于卸载证书注册策略（Certificate Enrollment Policy, CEP）Web服务。

## 示例

### 示例 1：卸载 CEP Web Service 中的所有配置

```powershell
Uninstall-AdcsEnrollmentPolicyWebService -AllPolicyServers -Force
```

此命令会卸载 CEP Web 服务中的所有配置，而不会提示用户进行确认。

### 示例 2：卸载 CEP Web 服务的实例

```powershell
Uninstall-AdcsEnrollmentPolicyWebService -AuthenticationType Certificate -KeyBasedRenewal -Force
```

此命令会卸载使用证书认证机制且处于基于密钥的更新模式下的 CEP Web 服务实例，而不会提示用户进行确认。

## 参数

### -AllPolicyServers

表示该cmdlet会卸载所有CEP Web Service的实例。

```yaml
Type: SwitchParameter
Parameter Sets: UninstallAll
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AuthenticationType

当存在多个 CEP Web 服务实例时，该参数用于指定要卸载的实例的身份验证类型。

```yaml
Type: AuthenticationType
Parameter Sets: UninstallSingleInstance
Aliases:
Accepted values: Kerberos, UserName, Certificate

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm

在运行cmdlet之前会提示您确认是否要继续。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令运行，而不会询问用户的确认。

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

### -KeyBasedRenewal

表示该 cmdlet 会卸载正在基于密钥的更新模式下运行的 CEP Web Service 实例。此参数是可选的，用于在存在多个使用相同身份验证类型的实例时区分需要卸载的具体 CEP Web Service 实例。如果未指定此选项，则会卸载未启用 KeyBasedRenewal 模式的、且使用了所定义身份验证类型（AuthenticationType）的 CEP Web Service 实例。

```yaml
Type: SwitchParameter
Parameter Sets: UninstallSingleInstance
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.Management.Automation.SwitchParameter

### Microsoft.CertificateServices.Deployment(Common AuthenticationType

## 输出

### Microsoft.CertificateServices.Deployment(Common.CEP.EnrollmentPolicyServiceResult

## 备注

- Ensure you run Windows PowerShell as an administrator. You can use the **Force** parameter to
  bypass the prompt for confirmation.

## 相关链接

[安装 AdcsEnrollmentPolicyWebService](./Install-AdcsEnrollmentPolicyWebService.md)

