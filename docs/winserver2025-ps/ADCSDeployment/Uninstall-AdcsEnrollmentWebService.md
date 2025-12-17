---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Deployment.Commands.dll-Help.xml
Module Name: ADCSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsdeployment/uninstall-adcsenrollmentwebservice?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Uninstall-AdcsEnrollmentWebService
---

# 卸载 AdcsEnrollmentWebService

## 摘要
卸载“Certificate Enrollment Web服务”或其各个单独实例。

## 语法

### UninstallSingleInstance（默认选项）

```
Uninstall-AdcsEnrollmentWebService -CAConfig <String> -AuthenticationType <AuthenticationType>
 [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### UninstallAll

```
Uninstall-AdcsEnrollmentWebService [-AllEnrollmentServices] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Uninstall-AdcsEnrollmentWebService` cmdlet 可以卸载证书注册 Web 服务：要么完全删除所有相关实例，要么仅删除部分实例。

## 示例

### 示例 1：卸载所有与“Enrollment Web Service”相关的角色服务

```powershell
Uninstall-AdcsEnrollmentWebService -AllEnrollmentServices -Force
```

此命令会卸载所有“Enrollment Web Service”相关的角色服务，而不会提示用户进行确认。

### 示例 2：使用指定的 CA 卸载 Enrollment Web Service 角色服务

```powershell
$params = @{
    CAConfig           = "APP1.corp.contoso.com\corp-APP1-CA"
    AuthenticationType = Certificate
}
Uninstall-AdcsEnrollmentWebService @params
```

此命令使用名为 `APP1.corp.contoso.com\corp-APP1-CA` 的配置文件中指定的证书颁发机构（CA）来卸载“证书注册Web服务”。该CA配置文件包含证书颁发机构的计算机名称和通用名称，两者之间用反斜杠分隔。所使用的身份验证类型是“证书”（Certificate）。

## 参数

### -AllEnrollmentServices

表示此cmdlet会删除所有证书注册Web服务实例。

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

指定要卸载的注册服务实例的身份验证类型。

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

### -CAConfig

指定用于卸载注册服务的证书颁发机构（CA）的配置字符串。当存在多个证书注册Web服务实例时，此参数用于确定要卸载哪个具体的实例。

```yaml
Type: String
Parameter Sets: UninstallSingleInstance
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm

在运行cmdlet之前会提示您进行确认。

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

强制命令运行，而无需请求用户确认。

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

### -WhatIf

展示了如果该cmdlet被运行时会发生什么情况。但实际上该cmdlet并未被运行。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### Microsoft.CertificateServices.Deployment COMMONAuthenticationType

### System.Management.Automation.SwitchParameter

## 输出

### Microsoft.CertificateServices.Deployment COMMON.CES.EnrollmentServiceResult

## 备注

- The application directories are removed from their respective instance folders in the file system.
  The uninstall command does not remove the Secure Sockets Layer/Transport Layer Security (SSL/TLS)
  or the secure hypertext transfer protocol (https) bindings.

## 相关链接

[安装 AdcsEnrollmentWebService](./Install-AdcsEnrollmentWebService.md)
