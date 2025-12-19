---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmreplicationserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMReplicationServer
---

# 获取虚拟机复制服务器信息

## 摘要
获取副本服务器的复制和认证设置信息。

## 语法

### ComputerName（默认值）
```
Get-VMReplicationServer [[-ComputerName] <String[]>] [[-Credential] <PSCredential[]>] [<CommonParameters>]
```

### CimSession
```
Get-VMReplicationServer [-CimSession] <CimSession[]> [<CommonParameters>]
```

## 描述
`Get-VMReplicationServer` cmdlet 可以获取复制服务器的复制和身份验证设置。

## 示例

### 示例 1
```
PS C:\> Get-VMReplicationServer
```

这个示例获取了本地副本服务器（Replica Server）的复制配置信息。

### 示例 2
```
PS C:\> Get-VMReplicationServer server01.domain01.contoso.com
```

这个示例获取了名为 server01.domain01.contoso.com 的服务器的复制配置信息。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如使用[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet得到的结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: CimSession
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此cmdlet的Hyper-V主机。可以使用NetBIOS名称、IP地址或完全合格的域名来进行指定。默认值是本地计算机。可以使用“localhost”或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: ComputerName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: ComputerName
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMReplicationServer

## 备注

## 相关链接

