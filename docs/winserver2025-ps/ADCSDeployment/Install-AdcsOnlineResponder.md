---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.CertificateServices.Deployment.Commands.dll-Help.xml
Module Name: ADCSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/adcsdeployment/install-adcsonlineresponder?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-AdcsOnlineResponder
---

# 安装 AdcsOnlineResponder

## 摘要
安装在线响应器服务。

## 语法

```
Install-AdcsOnlineResponder [-Force] [-Credential <PSCredential>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述

`Install-AdcsOnlineResponder` cmdlet 用于安装在线响应器（Online Responder）服务，该服务提供在线证书状态协议（OSCP）相关功能。若要卸载此角色服务，请使用 `Uninstall-AdcsOnlineResponder` cmdlet。

您可以通过在 Windows PowerShell 中运行以下命令来导入该 cmdlet：

- `Import-Module ServerManager`
- `Add-WindowsFeature Adcs-Online-Cert`

## 示例

### 示例 1：安装“在线响应程序”角色服务

```powershell
Install-AdcsOnlineResponder
```

此命令用于安装“在线响应程序”（Online Responder）角色服务。

### 示例 2：强制安装“在线响应程序”角色服务

```powershell
Install-AdcsOnlineResponder -Force
```

此命令会强制安装“在线响应程序”角色服务。

## 参数

### -Confirm

在运行cmdlet之前，会提示您确认是否要继续执行该操作。

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

### -Credential

为在线响应器服务指定一个 **PSCredential** 对象。要获取该凭据对象，请使用 `Get-Credential` cmdlet。有关更多信息，请输入 `Get-Help Get-Credential`。您只能在属于 Active Directory 域服务 (AD DS) 域的服务器上安装在线响应器角色服务。如果您要安装的在线响应器配置为使用独立的证书颁发机构 (CA)，则需要目标服务器上的本地 Administrators 组成员账户；如果您要安装的在线响应器用于连接到企业级证书颁发机构 (Enterprise CA)，则需要目标服务器上的 Domain Admins 组成员账户。

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

展示了如果运行该cmdlet会发生什么情况。不过实际上并没有运行该cmdlet。

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

此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.Management Automation.PSCredential

## 输出

### Microsoft.CertificateServices.Deployment COMMON.OCSP.OnlineResponderResult

## 备注

- Ensure you run Windows PowerShell as an administrator. You can use the **Force** parameter to
  bypass the prompt for confirmation. To see parameters, run the following command:

    `Install-AdcsOnlineResponder -?`

## 相关链接

[卸载 AdcsOnlineResponder](./Uninstall-AdcsOnlineResponder.md)

[获取凭据](https://go.microsoft.com/fwlink/?LinkID=293936)
