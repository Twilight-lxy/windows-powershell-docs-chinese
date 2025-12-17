---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Deployment.Commands.dll-Help.xml
Module Name: ADCSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsdeployment/install-adcswebenrollment?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-AdcsWebEnrollment
---

# 安装 AdcsWebEnrollment

## 摘要
安装证书颁发机构（CA）的Web注册功能。

## 语法

```
Install-AdcsWebEnrollment [-CAConfig <String>] [-Force]
 [-Credential <PSCredential>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Install-AdcsWebEnrollment` cmdlet 用于初始化安装和配置证书颁发机构（CA）的 Web Enrollment 角色服务。若要删除该 Web Enrollment 角色服务，请使用 `Uninstall-AdcsWebEnrollment` cmdlet。

您可以通过在 Windows PowerShell 中运行以下命令来导入该 cmdlet：

- `Import-Module ServerManager`
- `Add-WindowsFeature Adcs-Web-Enrollment`

## 示例

### 示例 1：将“Web Enrollment”角色服务安装到具有确认功能的证书颁发机构（CA）上

```powershell
Install-AdcsWebEnrollment -CAConfig "<CAComputerName>\<CACommonName>"
```

此命令会将“Web Enrollment”角色服务安装到由 `<CAComputerName>\<CACommonName>` 指定的证书颁发机构（CA）上。在运行该命令时，请将 `<CAComputerName>` 替换为实际的 CA 机器名称，将 `<CACommonName>` 替换为对应的 CA 公共名称。

### 示例 1：在没有确认的情况下将“Web Enrollment”角色服务安装到证书颁发机构（CA）上

```powershell
Install-AdcsWebEnrollment -CAConfig "<CAComputerName>\<CACommonName>" -Force
```

该命令会将“Web Enrollment”角色服务安装到由 `<CAComputerName>\<CACommonName>` 指定的证书颁发机构（CA）上，无需用户确认。运行命令时，请将 `<CAComputerName>` 替换为实际的 CA 电脑名称，并将 `<CACommonName>` 替换为对应的 CA 公共名称。

## 参数

### -CAConfig

指定CA配置参数字符串。如果已经安装了本地CA，请不要指定此参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential

指定一个用于 CA（证书颁发机构）Web 注册的 **PSCredential** 对象。要获取该凭据对象，请使用 `Get-Credential` cmdlet。有关更多信息，请输入 `Get-Help Get-Credential`。如果 Web 注册服务配置为使用独立的 CA，则需要一个属于本地 Administrators 组的账户；如果 Web 注册服务配置为使用企业级 CA（Enterprise CA），则需要一个属于 Domain Admins 组的账户。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Force

强制命令执行，而无需请求用户确认。

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

展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

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

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.Management.Automation.PSCredential

## 输出

### Microsoft.CertificateServices.Deployment(Common.WEP.WebEnrollmentResult

## 备注

- Ensure you run Windows PowerShell as an administrator. You can use the **Force** parameter to
  bypass the prompt for confirmation. To see parameters, run the following command:

    `Install-AdcsWebEnrollment -?`

## 相关链接

[卸载 AdcsWebEnrollment](./Uninstall-AdcsWebEnrollment.md)

[Get-Credential](https://go.microsoft.com/fwlink/?LinkID=293936)
