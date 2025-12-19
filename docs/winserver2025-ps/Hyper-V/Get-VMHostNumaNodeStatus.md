---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmhostnumanodestatus?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMHostNumaNodeStatus
---

# 获取虚拟机主机 NUMA 节点状态

## 摘要
获取虚拟机主机上非统一内存访问（NUMA）节点的状态。

## 语法

### ComputerName（默认值）
```
Get-VMHostNumaNodeStatus [[-ComputerName] <String[]>] [[-Credential] <PSCredential[]>] [-Id <Int32>]
 [<CommonParameters>]
```

### CimSession
```
Get-VMHostNumaNodeStatus [-CimSession] <CimSession[]> [-Id <Int32>] [<CommonParameters>]
```

## 描述
`Get-VMHostNumaNodeStatus` cmdlet 用于获取虚拟机主机上那些支持非统一内存访问（NUMA）技术的虚拟机的状态。如果该虚拟机主机启用了 NUMA 技术，那么使用此 cmdlet 会返回错误信息。

## 示例

### 示例 1
```
PS C:\> Get-VMHostNumaNodeStatus
```

获取本地Hyper-V主机上采用非统一内存访问（NUMA）技术的虚拟机的状态信息。

## 参数

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。请输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: CimSession
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此 cmdlet 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名来进行指定。默认值为本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: ComputerName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
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

### -Id
用于确定要获取虚拟机状态的 NUMA 节点。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShellcommands.GetVMHostNumaNodeStatus

## 备注

## 相关链接

